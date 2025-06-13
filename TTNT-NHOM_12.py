def in_board(board):
    for hang in board:
        print("|".join(hang))
        print("-" * 5)

def kiem_tra_thang(board, nguoi_choi):
    dieu_kien_thang = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
    ]
    for dieu_kien in dieu_kien_thang:
        if all(board[h][c] == nguoi_choi for h, c in dieu_kien):
            return True
    return False

def kiem_tra_hoa(board):
    return all(o != ' ' for hang in board for o in hang)

def tim_kiem_dfs(board, nguoi_choi):
    if kiem_tra_thang(board, 'X'):
        return 1
    if kiem_tra_thang(board, 'O'):
        return -1
    if kiem_tra_hoa(board):
        return 0
    nguoi_tiep_theo = 'O' if nguoi_choi == 'X' else 'X'
    cac_diem = []
    for hang in range(3):
        for cot in range(3):
            if board[hang][cot] == ' ':
                board[hang][cot] = nguoi_choi
                diem = tim_kiem_dfs(board, nguoi_tiep_theo)
                cac_diem.append(diem)
                board[hang][cot] = ' '
    if not cac_diem:
        return 0
    return max(cac_diem) if nguoi_choi == 'X' else min(cac_diem)

def AI_move(board):
    diem_tot_nhat = -float('inf')
    move = None

    for hang in range(3):
        for cot in range(3):
            if board[hang][cot] == ' ':
                board[hang][cot] = 'X'
                diem = tim_kiem_dfs(board, 'O')
                board[hang][cot] = ' '
                if diem > diem_tot_nhat:
                    diem_tot_nhat = diem
                    move = (hang, cot)
    if move:
        board[move[0]][move[1]] = 'X'

def nguoi_choi_move(board):
    while True:
        try:
            vi_tri = input("Nhập vị trí đánh (hàng cột), mỗi giá trị từ 0 đến 2, cách nhau bằng dấu cách: ")
            hang, cot = map(int, vi_tri.strip().split())

            if 0 <= hang < 3 and 0 <= cot < 3 and board[hang][cot] == ' ':
                board[hang][cot] = 'O'
                break
            else:
                print(" Vị trí không hợp lệ hoặc ô đã có người đánh. Vui lòng thử lại.")
        except:
            print(" Lỗi định dạng! Nhập lại theo cú pháp: số_hàng số_cột (VD: 1 2)")

def main():
    board = [[' '] * 3 for _ in range(3)]

    print(" Bạn là người chơi 'O', AI là 'X'.")
    in_board(board)

    while True:
        nguoi_choi_move(board)
        print("\n Bàn cờ sau lượt đi của bạn:")
        in_board(board)

        if kiem_tra_thang(board, 'O'):
            print(" Bạn đã chiến thắng!")
            break

        if kiem_tra_hoa(board):
            print("Trò chơi hòa. ")
            break

        AI_move(board)
        print(" Bàn cờ sau lượt đi của AI:")
        in_board(board)

        if kiem_tra_thang(board, 'X'):
            print(" AI đã thắng!")
            break

        if kiem_tra_hoa(board):
            print(" Trò chơi hòa.")
            break

if __name__ == "__main__":
    main()
