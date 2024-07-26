import numpy as np
from sklearn.decomposition import TruncatedSVD
movies = [
    {"title": "Dilwale Dulhania Le Jayenge", "genre": "Romance", "rating": 8.2},
    {"title": "Lagaan", "genre": "Drama", "rating": 8.1},
    {"title": "3 Idiots", "genre": "Comedy", "rating": 8.4},
    {"title": "Dangal", "genre": "Sports", "rating": 8.4},
    {"title": "Kuch Kuch Hota Hai", "genre": "Romance", "rating": 7.6}
]
books = [
    {"title": "To Kill a Mockingbird", "genre": "Fiction", "rating": 9.0},
    {"title": "1984", "genre": "Dystopian", "rating": 8.9},
    {"title": "Pride and Prejudice", "genre": "Romance", "rating": 9.1},
    {"title": "The Great Gatsby", "genre": "Classic", "rating": 8.8},
    {"title": "Moby-Dick", "genre": "Adventure", "rating": 7.5}
]
it_products = [
    {"name": "Laptop A", "category": "Laptop", "rating": 8.5},
    {"name": "Smartphone B", "category": "Smartphone", "rating": 9.1},
    {"name": "Tablet C", "category": "Tablet", "rating": 8.0},
    {"name": "Smartwatch D", "category": "Smartwatch", "rating": 7.8},
    {"name": "Headphones E", "category": "Accessories", "rating": 8.3}
]
items = movies + books + it_products
item_names = [item.get("title") or item.get("name") for item in items]
np.random.seed(42)
user_item_ratings = np.random.randint(1, 10, size=(5, len(items)))  
svd = TruncatedSVD(n_components=3, random_state=42)
latent_factors = svd.fit_transform(user_item_ratings)
def recommend_items_to_user(user_id, user_item_matrix, item_names, top_n=5):
    user_latent_factors = latent_factors[user_id]
    item_latent_factors = svd.components_.T
    scores = user_latent_factors.dot(item_latent_factors.T)
    item_indices = np.argsort(scores)[-top_n:][::-1]
    return [item_names[i] for i in item_indices]
print("Welcome to SherlockRecommendationAI!")
print("Created by Sayar Basu.")
print("This AI system will recommend movies, books, or IT products based on your preferences.\n")
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}!\n")
category = input("Enter the category you'd like recommendations for (movies/books/IT products): ").strip().lower()
preference = input("Enter your preference in the form of ratings (e.g., 8+) or genre/category (e.g., Romance/Laptop): ").strip().lower()
if category == "movies":
    data = movies
    key = "genre"
    recommendation_key = "title"
elif category == "books":
    data = books
    key = "genre"
    recommendation_key = "title"
elif category == "it products":
    data = it_products
    key = "category"
    recommendation_key = "name"
else:
    print("Invalid category. Exiting.")
    exit()
def filter_recommendations(data, user_preference, preference_type):
    if preference_type == "rating":
        recommendations = [entry for entry in data if entry.get("rating") >= float(user_preference)]
    else:
        recommendations = [entry for entry in data if user_preference in entry.get(key, "").lower()]
    return recommendations
filtered_recommendations = filter_recommendations(data, preference, "genre" if not preference.isnumeric() else "rating")
print(f"\nRecommended {category.capitalize()}:")
if filtered_recommendations:
    for item in filtered_recommendations:
        print(f"{item.get(recommendation_key)} - {item.get(key).capitalize()} - Rating: {item.get('rating')}")
else:
    print("No recommendations found based on your preferences.")
