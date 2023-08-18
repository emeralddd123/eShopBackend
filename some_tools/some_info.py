import random

store_data = [
    {
        "email": "applestore@example.com",
        "password": "applepassword",
        "store_name": "Apple Store",
        "description": "Official store for Apple products and accessories."
    },
    {
        "email": "fashionhub@example.com",
        "password": "fashionpassword",
        "store_name": "Fashion Hub",
        "description": "Trendy clothing and fashion accessories for all ages."
    },
    {
        "email": "homewonders@example.com",
        "password": "homepassword",
        "store_name": "Home Wonders",
        "description": "A wide range of home decor and kitchen essentials."
    },
    {
        "email": "bookworms@example.com",
        "password": "bookpassword",
        "store_name": "Bookworms",
        "description": "Explore a world of books from various genres."
    },
    {
        "email": "beautyessentials@example.com",
        "password": "beautypassword",
        "store_name": "Beauty Essentials",
        "description": "Quality beauty products for skincare and cosmetics."
    },
    {
        "email": "outdoorsupplies@example.com",
        "password": "outdoorpassword",
        "store_name": "Outdoor Supplies",
        "description": "Gear up for outdoor adventures with our products."
    },
    {
        "email": "autopartsplus@example.com",
        "password": "autopassword",
        "store_name": "Auto Parts Plus",
        "description": "Get high-quality auto parts and accessories."
    },
    {
        "email": "toyland@example.com",
        "password": "toypassword",
        "store_name": "Toyland",
        "description": "A magical place for toys and games enthusiasts."
    },
    {
        "email": "jewelrygems@example.com",
        "password": "jewelpassword",
        "store_name": "Jewelry Gems",
        "description": "Find exquisite jewelry pieces for every occasion."
    },
    {
        "email": "petsparadise@example.com",
        "password": "petspassword",
        "store_name": "Pets Paradise",
        "description": "Everything you need for your beloved pets."
    },
    {
        "email": "babybliss@example.com",
        "password": "babypassword",
        "store_name": "Baby Bliss",
        "description": "Discover a world of joy with our baby products."
    },
    {
        "email": "officesuppliesco@example.com",
        "password": "officepassword",
        "store_name": "Office Supplies Co.",
        "description": "Equip your workspace with our office supplies."
    },
    {
        "email": "gourmetdelights@example.com",
        "password": "gourmetpassword",
        "store_name": "Gourmet Delights",
        "description": "Indulge in a variety of gourmet food and beverages."
    },
    {
        "email": "toolsgalore@example.com",
        "password": "toolspassword",
        "store_name": "Tools Galore",
        "description": "Find the right tools for your DIY projects and repairs."
    },
    {
        "email": "moviemania@example.com",
        "password": "moviepassword",
        "store_name": "Movie Mania",
        "description": "Enjoy the latest movies and TV shows at home."
    },
    {
        "email": "musicworld@example.com",
        "password": "musicpassword",
        "store_name": "Music World",
        "description": "Explore a wide selection of music albums and instruments."
    },
    {
        "email": "furnitureplus@example.com",
        "password": "furniturepassword",
        "store_name": "Furniture Plus",
        "description": "Furnish your home with our stylish furniture options."
    },
    {
        "email": "techwizards@example.com",
        "password": "techpassword",
        "store_name": "Tech Wizards",
        "description": "Stay updated with the latest tech gadgets and accessories."
    },
    {
        "email": "artcrafters@example.com",
        "password": "artpassword",
        "store_name": "Art Crafters",
        "description": "Discover your artistic side with our art supplies."
    },
    {
        "email": "sportszone@example.com",
        "password": "sportspassword",
        "store_name": "Sports Zone",
        "description": "Gear up for your favorite sports and outdoor activities."
    },
    {
        "email": "giftexpress@example.com",
        "password": "giftpassword",
        "store_name": "Gift Express",
        "description": "Find the perfect gift for your loved ones."
    }
]

#for ven in store_data:
#    vend = Vendor(store_name=ven["store_name"],email=ven["email"],password=ven["password"],description=ven["description"])

product_categories = [
    {
        "name": "Electronics",
        "description": "Products related to electronic devices and technology."
    },
    {
        "name": "Clothing",
        "description": "Apparel and accessories for men, women, and children."
    },
    {
        "name": "Home and Kitchen",
        "description": "Items for home decor, cooking, and kitchen appliances."
    },
    {
        "name": "Books",
        "description": "Books of various genres, including fiction and non-fiction."
    },
    {
        "name": "Health and Beauty",
        "description": "Beauty products, personal care items, and health-related products."
    },
    {
        "name": "Sports and Outdoors",
        "description": "Sports equipment, outdoor gear, and recreational products."
    },
    {
        "name": "Automotive",
        "description": "Auto parts, accessories, and related products for vehicles."
    },
    {
        "name": "Toys and Games",
        "description": "Toys, games, and playthings for kids and adults."
    },
    {
        "name": "Jewelry",
        "description": "Various types of jewelry, including necklaces, rings, and bracelets."
    },
    {
        "name": "Pet Supplies",
        "description": "Supplies and accessories for pets, such as food, toys, and grooming products."
    },
    {
        "name": "Baby Products",
        "description": "Products for infants and babies, including clothing, toys, and nursery items."
    },
    {
        "name": "Office Supplies",
        "description": "Supplies and equipment for offices and workspaces."
    },
    {
        "name": "Grocery and Gourmet",
        "description": "Food and beverages, including gourmet and specialty items."
    },
    {
        "name": "Tools and Home Improvement",
        "description": "Tools, hardware, and products for home improvement projects."
    },
    {
        "name": "Movies and TV",
        "description": "Movies, TV shows, and related media in physical or digital format."
    },
    {
        "name": "Musical Instruments",
        "description": "Musical instruments and equipment for musicians and music enthusiasts."
    },
    {
        "name": "Furniture",
        "description": "Furniture items for homes, offices, and outdoor spaces."
    },
    {
        "name": "Industrial and Scientific",
        "description": "Products and equipment used in industrial and scientific fields."
    },
    {
        "name": "Arts and Crafts",
        "description": "Supplies, materials, and tools for arts, crafts, and DIY projects."
    },
    {
        "name": "Computers",
        "description": "Computer systems, laptops, and accessories."
    },
    {
        "name": "Software",
        "description": "Software programs, applications, and digital solutions."
    },
    {
        "name": "Appliances",
        "description": "Household appliances for various purposes."
    },
    {
        "name": "Cell Phones and Accessories",
        "description": "Cell phones, smartphones, and related accessories."
    },
    {
        "name": "Camera and Photo",
        "description": "Cameras, photography equipment, and accessories."
    },
    {
        "name": "Video Games",
        "description": "Video games for consoles, PCs, and other platforms."
    },
    {
        "name": "Beauty and Personal Care",
        "description": "Beauty products, skincare items, and personal care essentials."
    },
    {
        "name": "Shoes",
        "description": "Footwear for men, women, and children."
    },
    {
        "name": "Watches",
        "description": "Wristwatches and timepieces for different styles and purposes."
    },
    {
        "name": "Patio, Lawn, and Garden",
        "description": "Products for outdoor spaces, gardening, and landscaping."
    },
    {
        "name": "Hobbies",
        "description": "Items and equipment for various hobbies and recreational activities."
    },
    {
        "name": "Music",
        "description": "Music albums, recordings, and digital downloads."
    },
    {
        "name": "Collectibles",
        "description": "Unique and rare collectible items of interest."
    },
    {
        "name": "Food and Beverage",
        "description": "Food and beverages, including snacks and drinks."
    },
    {
        "name": "Gift Cards",
        "description": "Gift cards that can be used to purchase products or services."
    }
]


product_data = [
    {"vendor_id":1,

        "name": "Apple iPhone 12",
        "description": "The Apple iPhone 12 features a Super Retina XDR display, A14 Bionic chip, and a dual-camera system.",
        "sku": "APL-IPHONE12-BLK-64GB",
        "price": 999.99,
        "categories": ["Electronics", "Smartphones"]
    },
    {"vendor_id":1,

        "name": "Samsung Galaxy Watch",
        "description": "The Samsung Galaxy Watch offers a sleek design, heart rate monitoring, and built-in GPS.",
        "sku": "SAM-GALAXYWATCH-SLV",
        "price": 299.99,
        "categories": ["Electronics", "Wearable Technology"]
    },
    {"vendor_id":1,

        "name": "Nike Air Max 270",
        "description": "The Nike Air Max 270 provides maximum comfort and style with its visible Max Air unit and breathable mesh upper.",
        "sku": "NIK-AIRMAX270-BLK-WHT-10",
        "price": 149.99,
        "categories": ["Clothing", "Shoes"]
    },
    {"vendor_id":1,

        "name": "Canon EOS Rebel T7i",
        "description": "The Canon EOS Rebel T7i is a versatile DSLR camera with a 24.2MP sensor and a vari-angle touchscreen LCD.",
        "sku": "CAN-EOSREBELT7I-KIT",
        "price": 899.99,
        "categories": ["Electronics", "Cameras"]
    },
    {"vendor_id":1,

        "name": "Sony PlayStation 5",
        "description": "The Sony PlayStation 5 delivers immersive gaming experiences with its high-performance CPU, GPU, and SSD storage.",
        "sku": "SNY-PS5-STD-1TB",
        "price": 499.99,
        "categories": ["Electronics", "Gaming"]
    },
]

# Generating additional product dictionaries
def random_product():
    for i in range(5, 100):
        categories = random.sample(product_categories, random.randint(1, 5))
        category_names = [category["name"] for category in categories]
        "vendor_id":1,prod
        uct "vendor_id":1,= {

            "name": f"Product {i+1}",
            "description": f"This is the description for Product {i+1}.",
            "sku": f"sku{i+1:03}",
            "price": round(random.uniform(1.0, 500.0), 2),
            "categories": category_names
        }
        product_data.append(product)


import os

current_directory = os.getcwd()
# Generate 10 random numbers

# Save output to a text file
file_path = os.path.join(current_directory, 'product_sample.txt')
def generate_product(file_path, product_data):
    with open(file_path, 'w') as file:
        file.write(str(product_data))
        file.close()
    print("Random product generated and saved to 'product_sample.txt' file.")


products = [
    {
        "vendor_id":1,
        "name": "iPhone 14 Pro Max",
        "description": "The most advanced iPhone ever.",
        "quantity": 10,
        "sku": "1234567890",
        "price": 1099,
    },
    {
        "vendor_id":1,
        "name": "MacBook Pro M2",
        "description": "The most powerful MacBook Pro ever.",
        "quantity": 5,
        "sku": "9876543210",
        "price": 1999,
    },
    {
        "vendor_id":1,
        "name": "iPad Pro M2",
        "description": "The most versatile iPad ever.",
        "quantity": 20,
        "sku": "0987654321",
        "price": 899,
    },
    {
        "vendor_id":1,
        "name": "Apple Watch Series 8",
        "description": "The most advanced Apple Watch yet.",
        "quantity": 30,
        "sku": "1234567891",
        "price": 399,
    },
    {
        "vendor_id":1,
        "name": "AirPods Pro",
        "description": "The best wireless earbuds ever.",
        "quantity": 40,
        "sku": "9876543211",
        "price": 249,
    },
    {
        "vendor_id":1,
        "name": "HomePod Mini",
        "description": "The perfect smart speaker for any room.",
        "quantity": 50,
        "sku": "0987654322",
        "price": 99,
    },
    {
        "vendor_id":1,
        "name": "Apple TV 4K",
        "description": "The best streaming device on the market.",
        "quantity": 100,
        "sku": "1234567892",
        "price": 199,
    },
    {
        "vendor_id":1,
        "name": "Beats Studio Buds",
        "description": "The best wireless earbuds for working out.",
        "quantity": 200,
        "sku": "9876543212",
        "price": 149,
    },
    {
        "vendor_id":1,
        "name": "MagSafe Battery Pack",
        "description": "The perfect way to extend your iPhone's battery life.",
        "quantity": 100,
        "sku": "0987654323",
        "price": 99,
    },
    {
        "vendor_id":1,
        "name": "Magic Keyboard for iPad Pro",
        "description": "The perfect keyboard for your iPad Pro.",
        "quantity": 50,
        "sku": "1234567893",
        "price": 349,
    },
    {
        "vendor_id":1,
        "name": "Magic Trackpad for Mac",
        "description": "The perfect trackpad for your Mac.",
        "quantity": 25,
        "sku": "9876543213",
        "price": 199,
    },
    {
        "vendor_id":1,
        "name": "Apple Pencil (2nd generation)",
        "description": "The perfect stylus for your iPad Pro.",
        "quantity": 100,
        "sku": "0987654324",
        "price": 129,
    },
    {
        "vendor_id":1,
        "name": "AirPods Max",
        "description": "The best wireless headphones ever.",
        "quantity": 50,
        "sku": "1234567894",
        "price": 549,
    },
    {
        "vendor_id":1,
        "name": "Apple Watch SE",
        "description": "The perfect Apple Watch for everyone.",
        "quantity": 100,
        "sku": "9876543214",
        "price": 279,
    },
        {
        "vendor_id":1,
        "name": "iPad Air (5th generation)",
        "description": "The perfect iPad for students and creatives.",
        "quantity": 200,
        "sku": "0987654325",
        "price": 599,
    },
    {
        "vendor_id":1,
        "name": "iMac (24-inch, M1)",
        "description": "The perfect all-in-one desktop computer for your home.",
        "quantity": 100,
        "sku": "1234567895",
        "price": 1299,
    },
    {
        "vendor_id":1,
        "name": "MacBook Air M2",
        "description": "The most powerful MacBook Air ever.",
        "quantity": 50,
        "sku": "9876543215",
        "price": 999,
    },
    {
        "vendor_id":1,
        "name": "Studio Display",
        "description": "The perfect monitor for your Mac.",
        "quantity": 100,
        "sku": "0987654326",
        "price": 1599,
    },
    {
        "vendor_id":1,
        "name": "iPhone 14",
        "description": "The most advanced iPhone yet.",
        "quantity": 100,
        "sku": "1234567896",
        "price": 799,
    },
    {
        "vendor_id":1,
        "name": "iPad mini (6th generation)",
        "description": "The perfect iPad for kids and travelers.",
        "quantity": 200,
        "sku": "9876543216",
        "price": 499,
    },
    {
        "vendor_id":1,
        "name": "Apple Watch Series 7",
        "description": "The most advanced Apple Watch yet.",
        "quantity": 300,
        "sku": "0987654327",
        "price": 399,
    },
    {
        "vendor_id":1,
        "name": "AirPods 3",
        "description": "The best wireless earbuds for most people.",
        "quantity": 400,
        "sku": "1234567897",
        "price": 199,
    },
    {
        "vendor_id":1,
        "name": "HomePod",
        "description": "The perfect smart speaker for small spaces.",
        "quantity": 500,
        "sku": "9876543217",
        "price": 99,
    },
]


print(len(products))