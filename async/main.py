import asyncio
import time

test_product = {
    'name': 'Test Product'
}

async def add_quantity_data(product):
    quantity = 5
    print('Adding quantity data...')
    await asyncio.sleep(1)
    product['quantity'] = quantity
    print("Quantity data added!!!")
    
async def add_pricing_data(product):
    price = 'Ghs5'
    print('Getting pricing data...')
    await asyncio.sleep(1.5)
    product['price'] = price
    print("Pricing data added!!!")
    
async def run_in_parallel(*functions):
    await asyncio.gather(*functions)
    
async def run_in_sequence(*functions):
    for function in functions:
        await function
        
        
# async def main():
#     # Running in sequence
#     t1 = time.perf_counter()
#     await run_in_sequence(
#         add_pricing_data(test_product),
#         add_quantity_data(test_product)
#     )
#     t2 = time.perf_counter()
#     print("Running in sequence: ", t2-t1)
    
#     #Running in parallel
#     t1 = time.perf_counter()
#     await run_in_parallel(
#         add_pricing_data(test_product),
#         add_quantity_data(test_product)
#     )
#     t2 = time.perf_counter()
#     print("Running in parallel: ", t2-t1)
    
async def main():
    # t1 = asyncio.create_task(add_pricing_data(test_product))
    # t2 = asyncio.create_task(add_quantity_data(test_product))
    
    await asyncio.gather(add_pricing_data(test_product), add_quantity_data(test_product))
    
    
asyncio.run(main())
# main()

