import asyncio
import chess
import chess.engine

async def main() -> None:
    transport, engine = await chess.engine.popen_uci("engine/stockfish.exe")

    board = chess.Board()
    print(board.turn == chess.BLACK)
    info = await engine.analyse(board, chess.engine.Limit(time=0.1))
    print(info["score"])
    # Score: PovScore(Cp(+20), WHITE)

    board = chess.Board("r1bqkbnr/p1pp1ppp/1pn5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 2 4")
    info = await engine.analyse(board, chess.engine.Limit(depth=20))
    print(info["score"])
    # Score: PovScore(Mate(+1), WHITE)

    await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())