"""Module to run knights tour dynamic."""
N = 6 

NUM_EXPERIMENTS = 4

def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def get_degree(x, y, board, move_x, move_y):
    count = 0
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if is_safe(next_x, next_y, board):
            count += 1
    return count

def solve_kt_util(x, y, move_count, board, move_x, move_y, path_branch_factors):
    if move_count == N * N:
        return True

    possible_moves = []
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if is_safe(next_x, next_y, board):
            
            degree = get_degree(next_x, next_y, board, move_x, move_y)
            possible_moves.append((degree, next_x, next_y))
    
    possible_moves.sort()

    path_branch_factors.append(len(possible_moves))

    for _, next_x, next_y in possible_moves:
        board[next_x][next_y] = move_count
        
        if solve_kt_util(next_x, next_y, move_count + 1, board, move_x, move_y, path_branch_factors):
            return True
        else:
            
            board[next_x][next_y] = -1
            path_branch_factors.pop() 
    
    return False

def run_knight_tour_experiments():

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    
    all_tours_branch_factors = []
    num_tours_found = 0

    for i in range(NUM_EXPERIMENTS):
        print(f"=== PERCOBAAN {i + 1} dari {NUM_EXPERIMENTS} ===")

        start_x, start_y = -1, -1
        while True:
            try:
                sx_str = input(f"Masukkan baris awal (0-{N-1}): ")
                sy_str = input(f"Masukkan kolom awal (0-{N-1}): ")
                start_x = int(sx_str)
                start_y = int(sy_str)
                
                if 0 <= start_x < N and 0 <= start_y < N:
                    break
                else:
                    print(f"Input tidak valid. Harap masukkan angka antara 0 dan {N-1}.")
            except ValueError:
                print("Input tidak valid. Harap masukkan bilangan bulat saja.")
        
        
        board = [[-1 for _ in range(N)] for _ in range(N)]
        board[start_x][start_y] = 0
        path_branch_factors = []

        
        if solve_kt_util(start_x, start_y, 1, board, move_x, move_y, path_branch_factors):
            num_tours_found += 1
            print(f"\nPenjelajahan ke-{num_tours_found} BERHASIL ditemukan dari ({start_x}, {start_y}).\n")
            
            
            print("Papan Hasil Penjelajahan (0 = awal):")
            for row in range(N):
                for col in range(N):
                    print(f"{board[row][col]:>3}", end="")
                print()
            
            
            path_coords = [None] * (N * N)
            for row in range(N):
                for col in range(N):
                    if board[row][col] != -1:
                        path_coords[board[row][col]] = (row, col)
            
            print("\nBarisan Penjelajahan dalam Format Koordinat (baris, kolom):")
            sequence_str = " ".join([f"({r},{c})" for r, c in path_coords])
            print(f"( {sequence_str} )")
            
            

            all_tours_branch_factors.extend(path_branch_factors[:-1])

        else:
            print(f"\nGAGAL menemukan solusi dari titik awal ({start_x}, {start_y}).")
        
        print("=" * 50 + "\n")

    
    print("\n=== ANALISIS GABUNGAN & ESTIMASI SIZE TREE ===")

    if not all_tours_branch_factors:
        print("Tidak ada tur yang berhasil ditemukan dari semua eksperimen.")
        print("Tidak dapat mengestimasi ukuran pohon.")
        return

    
    avg_branch_factor = sum(all_tours_branch_factors) / len(all_tours_branch_factors)
    depth = N * N - 1
    estimated_tree_size = avg_branch_factor ** depth

    print(f"Total tur yang berhasil ditemukan: {num_tours_found} dari {NUM_EXPERIMENTS} percobaan.")
    print(f"Faktor Percabangan Rata-rata Gabungan (B): {avg_branch_factor:.4f}")
    print(f"Kedalaman Pohon (d): {depth}")
    
    print(f"Estimasi size tree ≈ B^d ≈ {estimated_tree_size}")



if __name__ == "__main__":
    run_knight_tour_experiments()
