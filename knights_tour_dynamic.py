"""Module to run knights tour dynamic."""
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

solutions = []
visited_count = 0

def is_safe(x, y, board, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def knight_tour(x, y, movei, board, path, N, max_solutions):
    global visited_count, solutions

    visited_count += 1

    board[x][y] = movei
    path.append((x, y))

    if movei == N * N - 1:
        solutions.append(path.copy())
        board[x][y] = -1
        path.pop()
        return

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if is_safe(nx, ny, board, N):
            knight_tour(nx, ny, movei + 1, board, path, N, max_solutions)
            if len(solutions) >= max_solutions:
                break

    board[x][y] = -1
    path.pop()

def main():
    global visited_count, solutions
    print("Knight's Tour Dinamis")

    try:
        N = int(input("Masukkan ukuran papan: "))
        max_solutions = int(input("Total solusi yang ingin dicari: "))
        start_x = int(input(f"Baris awal (0-{N-1}): "))
        start_y = int(input(f"Kolom awal (0-{N-1}): "))
        if not (0 <= start_x < N and 0 <= start_y < N):
            raise ValueError
    except ValueError:
        print("Input tidak valid. Gunakan angka yang sesuai dengan ukuran papan.")
        return

    board = [[-1 for _ in range(N)] for _ in range(N)]
    knight_tour(start_x, start_y, 0, board, [], N, max_solutions)

    if not solutions:
        print("Tidak ditemukan solusi.")
        return

    for idx, sol in enumerate(solutions):
        print(f"\nSolusi {idx + 1}:")
        for i, pos in enumerate(sol):
            print(f"{i+1:2}: {pos}", end="  ")
            if (i + 1) % N == 0:
                print()

    print(f"\nEstimasi total tree size (simpul eksplorasi): {visited_count}")

if __name__ == "__main__":
    main()
