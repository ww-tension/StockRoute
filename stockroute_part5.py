# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: StockRoute
def update_stock_route(route_id, updates):
    try:
        route = routes[route_id]
        if not route:
            print(f"Error: Route {route_id} not found.")
            return False
        
        for key, value in updates.items():
            if hasattr(route, key) and value is not None:
                setattr(route, key, value)
        
        routes[route_id] = route
        return True
    except KeyError as e:
        print(f"Error: Missing record or invalid field {e}.")
        return False
