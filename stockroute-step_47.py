# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: StockRoute
import stock_route as sr

demo = (
    sr.Demo("Morning run")
        .add_batch(sr.Batch(1, "Batches", 20))
        .add_stock("S1", sr.Stock(1, "Almonds", 50), transfer="Transfer A")
        .add_checkpoint(sr.Checkpoint("C1", "Warehouse"), exception=sr.ExceptionNote("C1 delayed"))
        .add_stock("S2", sr.Stock(2, "Rice", 30), transfer="Transfer B")
        .add_warehouse(sr.Warehouse("WH1", "Main warehouse"))
        .finish()
)

print(demo.to_csv())
