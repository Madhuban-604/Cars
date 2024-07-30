import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB connection URI
db = client["usersdata"]

# Create the cardetails collection
cardetails = db["cardetails"]

# Car data
cars_data = [
    {
        "name": "Standard Sedan",
        "model": "Basic Sedan Car",
        "price_per_hour": "₹1500",
        "description": "Standard sedans are versatile vehicles suitable for everyday commuting and small families. They offer a comfortable ride and economical fuel consumption.",
        "image_link": "https://example.com/standard_sedan_image.jpg"
    },
    {
        "name": "SUV",
        "model": "Sport Utility Vehicle",
        "price_per_hour": "₹2500",
        "description": "SUVs are robust vehicles designed to tackle various terrains and weather conditions. They offer ample space for passengers and cargo, making them ideal for outdoor adventures and family trips.",
        "image_link": "https://example.com/suv_image.jpg"
    },
    # Add similar entries for the remaining cars
    {
        "name": "Luxury",
        "model": "Luxury High-End Car",
        "price_per_hour": "₹4000",
        "description": "Luxury cars combine premium features, advanced technology, and superior performance. They provide a lavish driving experience with unmatched comfort, style, and sophistication.",
        "image_link": "https://example.com/luxury_image.jpg"
    },
    {
        "name": "Compact",
        "model": "Small, Economical Car",
        "price_per_hour": "₹1200",
        "description": "Compact cars are ideal for city driving and short trips. They offer fuel efficiency and easy maneuverability, making them suitable for urban commuters and budget-conscious travelers.",
        "image_link": "https://example.com/compact_image.jpg"
    },
    {
        "name": "Convertible",
        "model": "Convertible Roof Car",
        "price_per_hour": "₹3000",
        "description": "Convertibles provide an exhilarating driving experience with the option to enjoy open-air motoring. They are perfect for leisurely drives and exploring scenic routes.",
        "image_link": "https://example.com/convertible_image.jpg"
    },
    {
        "name": "Hatchback",
        "model": "Small Car with Rear Door",
        "price_per_hour": "₹1000",
        "description": "Hatchbacks offer a compact yet practical solution for daily commuting and city driving. They feature a rear door that provides easy access to cargo space, making them versatile for various tasks.",
        "image_link": "https://example.com/hatchback_image.jpg"
    },
    {
        "name": "Minivan",
        "model": "Spacious Family Car",
        "price_per_hour": "₹2000",
        "description": "Minivans are ideal for families and group travel, offering ample seating and cargo space. They provide comfort and convenience for long journeys and city outings.",
        "image_link": "https://example.com/minivan_image.jpg"
    },
    {
        "name": "Pickup Truck",
        "model": "Utility Vehicle with Open Bed",
        "price_per_hour": "₹3000",
        "description": "Pickup trucks are versatile vehicles suitable for transporting goods and equipment. They offer a spacious open bed for carrying cargo, making them essential for construction, landscaping, and recreational activities.",
        "image_link": "https://example.com/pickup_truck_image.jpg"
    },
    {
        "name": "Electric",
        "model": "Electric-Powered Car",
        "price_per_hour": "₹3500",
        "description": "Electric cars are eco-friendly vehicles powered by electric motors. They produce zero emissions and offer a quiet, smooth driving experience. They are suitable for urban commuting and contribute to reducing carbon footprint and air pollution.",
        "image_link": "https://example.com/electric_image.jpg"
    },
    {
        "name": "Limousine",
        "model": "Luxury Sedan with Extended Wheelbase",
        "price_per_hour": "₹5000",
        "description": "Limousines are premium luxury vehicles known for their spacious interiors and chauffeur-driven service. They offer utmost comfort, style, and sophistication, making them ideal for special events, corporate travel, and VIP transportation.",
        "image_link": "https://example.com/limousine_image.jpg"
    }
]

# Insert the car data into the cardetails collection
cardetails.insert_many(cars_data)

print("Car details inserted successfully.")