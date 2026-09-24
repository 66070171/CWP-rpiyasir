# ตัวอักษรที่นับว่าเป็นหมาก ใช้ตอบคำถามว่า "ช่องนี้มีอะไรขวางอยู่ไหม"
PIECES = "KQBRP"

# ก้าวเดินหนึ่งก้าวในรูป (row_step, col_step)
# row เพิ่ม = ลงล่าง, col เพิ่ม = ไปขวา

# ทิศทแยง 4 ทิศ ใช้กับ Bishop, Queen (และ Pawn ที่ระยะ 1)
DIAGONALS = ((-1, -1), (-1, 1), (1, -1), (1, 1))

# ทิศตรง 4 ทิศ ใช้กับ Rook, Queen
STRAIGHTS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def parse_board(board):
    # ด่านแรก ถ้าไม่ใช่ข้อความก็จบ ไม่งั้นบรรทัดถัดไปจะพังด้วย AttributeError
    if not isinstance(board, str):
        return None

    # จัดรูปแบบการขึ้นบรรทัดให้เป็นแบบเดียวกัน กันไฟล์ที่แก้มาจาก Windows
    # ถ้าปล่อยให้ \r ติดท้ายแถว ความยาวแถวจะเพี้ยนไป 1 ตัว
    rows = board.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    # ตัดบรรทัดว่างหัวท้ายทิ้ง เผื่อข้อความกระดานเขียนแบบ """ ขึ้นบรรทัดใหม่เลย
    # โดยไม่มีแบ็กสแลชปิดท้าย ซึ่งจะได้บรรทัดว่างแถมมาหัวหรือท้าย
    # บรรทัดว่างยาว 0 ตัวอักษร จึงเป็นส่วนหนึ่งของกระดานจัตุรัสไม่ได้อยู่แล้ว
    while rows and rows[-1] == "":
        rows.pop()
    while rows and rows[0] == "":
        rows.pop(0)

    if not rows:
        return None

    size = len(rows[0])
    if size == 0:
        return None

    # ทุกแถวต้องยาวเท่ากัน ไม่งั้นกระดานเป็นฟันปลา
    if any(len(row) != size for row in rows):
        return None

    # จำนวนแถวต้องเท่ากับความยาวแถว นี่คือความหมายของ "จัตุรัส"
    if len(rows) != size:
        return None

    # ต้องมี King เพียงตัวเดียว ไม่มีเลยก็ไม่รู้จะเช็คอะไร มีสองตัวก็ผิดกติกา
    if sum(row.count("K") for row in rows) != 1:
        return None

    return rows


def find_king(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "K":
                return row, col
    return None


def first_piece_on_path(board, row, col, row_step, col_step):
    size = len(board)
    distance = 1
    while True:
        next_row = row + row_step * distance
        next_col = col + col_step * distance

        # ออกนอกกระดานแล้ว แปลว่าทิศนี้ไม่มีหมากเลย
        # เงื่อนไขนี้ยังทำให้ while True จบเสมอ ไม่วนไม่รู้จบ
        # เพราะทุกทิศเดินออกจากจุดเริ่มต้น จึงหลุดขอบภายใน size รอบ
        if not (0 <= next_row < size and 0 <= next_col < size):
            return None, 0

        square = board[next_row][next_col]

        # ตัวอักษรที่ไม่ใช่หมากนับเป็นช่องว่าง เดินผ่านไปได้
        if square in PIECES:
            return square, distance

        distance += 1


def is_in_check(board):
    king_row, king_col = find_king(board)

    # แนวทแยง: Bishop กับ Queen กินได้ทุกระยะ ส่วน Pawn กินได้แค่ระยะ 1
    for row_step, col_step in DIAGONALS:
        piece, distance = first_piece_on_path(board, king_row, king_col, row_step, col_step)

        # ทิศนี้ว่างจนหลุดขอบ ข้ามไปดูทิศถัดไป
        # ต้องเช็คก่อนเทียบตัวอักษร ไม่งั้นจะเอา None ไปเทียบ
        if piece is None:
            continue

        if piece == "B" or piece == "Q":
            return True

        # เบี้ยกินเฉียงขึ้นบนระยะเดียวเท่านั้น (ความเป็นเส้นทแยงมาจากลูปนี้อยู่แล้ว)
        # row_step == 1 คือคัดเอาเฉพาะทิศทแยงล่าง เพราะเบี้ยที่อยู่ทแยงล่างของเรา
        # คือตัวที่กินเฉียงขึ้นมาโดนเราได้พอดี ส่วนเบี้ยที่อยู่ทแยงบนกินลงล่างไม่ได้
        if piece == "P" and distance == 1 and row_step == 1:
            return True

    # แนวตรง: Rook กับ Queen กินได้ทุกระยะ จึงไม่ต้องสนระยะห่าง
    for row_step, col_step in STRAIGHTS:
        piece, distance = first_piece_on_path(board, king_row, king_col, row_step, col_step)
        if piece == "R" or piece == "Q":
            return True

    # ครบทั้ง 8 ทิศแล้วไม่มีใครถึงตัว
    return False


def checkmate(board):
    chess_board = parse_board(board)
    if chess_board is None:
        return
    print("Success" if is_in_check(chess_board) else "Fail")
