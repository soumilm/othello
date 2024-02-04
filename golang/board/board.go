package board

type Cell int // Basically an enum representing the status of a cell

const (
	Invalid Cell = iota
	Empty
	BlackPiece
	WhitePiece
)

type Position struct {
	Row int
	Col int
}

const boardSize = 8
const boardArea = boardSize * boardSize

func (p *Position) valid() bool {
	if p.Row < 0 || p.Row >= boardSize {
		return false
	}
	if p.Col < 0 || p.Col >= boardSize {
		return false
	}
	return true
}

// Board consists of two uint64s, each representing the positions of all pieces
// of a given color. We treat a uint64 as a 64-bit vector, where the n-th least
// significant bit is 1 if there is a piece of that color.
//
// As an example, consider the 2x2 board below, and the bitvector representation.
//  +-------+
//  |   | B |
//  +-------+
//  | W | B |
//  +-------+
// {
//   Black: 10 // 0b0101
//   White: 4  // 0b0010
// }

type Board struct {
	Black uint64
	White uint64
}

func (b *Board) PieceAt(p *Position) Cell {
	if !p.valid() {
		return Invalid
	}

	cellNum := boardSize*p.Row + p.Col
	// We want the `cellNum`-th bit from the front, not the back
	index := boardArea - cellNum - 1 // 63 - cellNum

	isBlack := (b.Black >> index) & 1
	isWhite := (b.White >> index) & 1

	if isBlack == 1 {
		return BlackPiece
	} else if isWhite == 1 {
		return WhitePiece
	} else {
		return Empty
	}
}

// String returns a string representation of the board. This string should be a
// valid input to any future Python functionality to visualize Othello boards.
func (b *Board) String() string {
	return ""
}
