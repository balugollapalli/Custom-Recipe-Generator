import random

class RecipeGenerator:
    def __init__(self):
        # Expanded lists for more variety in recipes
        self.cooking_methods = ["sauté", "fry", "boil", "steam", "grill", "bake", "roast", "simmer", "stir-fry", "poach"]
        self.spices = ["turmeric", "red chili powder", "cumin seeds", "garam masala", "coriander powder", 
                       "black pepper", "paprika", "curry powder", "cinnamon", "cardamom", "cloves", "nutmeg"]
        self.herbs = ["coriander leaves", "mint", "basil", "parsley", "oregano", "thyme", "rosemary", "dill", "sage"]
        self.oils = ["sunflower oil", "mustard oil", "olive oil", "ghee", "coconut oil", "sesame oil", "avocado oil"]
        self.cooking_styles = ["Spicy", "Creamy", "Roasted", "Slow-Cooked", "Hearty", "Zesty", "Stir-Fried", 
                              "Grilled", "One-Pot", "Fusion", "Traditional", "Quick & Easy", "Gourmet", "Rustic"]
        self.dish_types = ["Curry", "Stew", "Soup", "Stir-Fry", "Salad", "Pasta", "Risotto", "Bowl", "Casserole", 
                          "Skillet Dish", "Bake", "Platter", "Pie", "Tart"]
        
        # New snack options
        self.snack_types = ["Dip", "Crisps", "Bites", "Rolls", "Fritters", "Skewers", "Toast", "Balls", "Chips", "Crackers"]
        self.snack_styles = ["Spicy", "Tangy", "Sweet", "Savory", "Crunchy", "Crispy", "Cheesy", "Zesty", "Herbed", "Smoky"]
        self.snack_methods = ["bake", "fry", "blend", "mix", "roast", "toast", "chill", "assemble", "layer", "roll"]
        
        # Ingredient categories for recipe type classification
        self.main_dish_indicators = ["chicken", "fish", "beef", "pork", "lamb", "mutton", "turkey", "shrimp", "salmon", 
                                     "pasta", "rice", "noodle", "potato", "carrot", "bell pepper", "tomato", "onion", 
                                     "quinoa", "lentil", "bean", "chickpea", "eggplant", "zucchini"]
        
        self.snack_indicators = ["nuts", "chips", "cracker", "seed", "popcorn", "pretzel", "chocolate", "cookie", "biscuit",
                                "crisp", "dried fruit", "granola", "trail mix", "yogurt", "cheese", "dip", "hummus", "salsa"]
                                
        self.sweet_indicators = ["sugar", "honey", "maple syrup", "chocolate", "cocoa", "vanilla", "cinnamon", 
                                "nutmeg", "banana", "apple", "berries", "fruit", "caramel", "dessert"]
        
        # Special ingredient handling dictionaries - detailed and practical instructions
        self.special_ingredients = {
            # Nuts and seeds
            "groundnut": {"prep": "use whole or coarsely crush in a mortar and pestle", 
                         "cook": "dry roast in a pan until fragrant, about 3-5 minutes"},
            "peanut": {"prep": "use whole or coarsely crush in a mortar and pestle", 
                      "cook": "dry roast in a pan until fragrant, about 3-5 minutes"},
            "almond": {"prep": "use whole, slice, or roughly chop based on preference", 
                      "cook": "toast in a dry pan until lightly golden, about 2-3 minutes"},
            "cashew": {"prep": "use whole or break into pieces by hand", 
                      "cook": "toast in a dry pan until golden, about 2-3 minutes"},
            "walnut": {"prep": "break into halves or quarters by hand", 
                      "cook": "toast briefly in a dry pan, about 1-2 minutes to enhance flavor"},
            "pistachio": {"prep": "remove shells and use whole", 
                         "cook": "use raw or lightly toast for 1-2 minutes"},
            "sesame seed": {"prep": "use as is", 
                           "cook": "toast in a dry pan until golden and fragrant, about 1-2 minutes"},
            
            # Grains
            "rice": {"prep": "rinse 2-3 times until water runs clear", 
                    "cook": "cook with 1:2 ratio of rice to water until fluffy"},
            "quinoa": {"prep": "rinse thoroughly under cold water", 
                      "cook": "cook with 1:2 ratio of quinoa to water for about 15 minutes"},
            "oat": {"prep": "measure out required amount", 
                   "cook": "simmer with 1:2 ratio of oats to liquid until creamy"},
            
            # Vegetables
            "onion": {"prep": "peel and finely dice or slice into rings as needed", 
                     "cook": "sauté until translucent or golden brown, about 3-5 minutes"},
            "tomato": {"prep": "wash and dice into small cubes, or slice for certain recipes", 
                      "cook": "cook until softened and slightly reduced, about 5-7 minutes"},
            "potato": {"prep": "wash, peel if desired, and cut into even-sized chunks", 
                      "cook": "boil until fork-tender, about 15-20 minutes, or roast until golden"},
            "carrot": {"prep": "peel and dice, julienne, or grate as needed", 
                      "cook": "cook until just tender but still retaining some crunch"},
            "chilli": {"prep": "remove stem, slice thinly or mince finely based on heat preference", 
                      "cook": "add early for more heat or later for milder flavor"},
            "red chilli": {"prep": "remove stem, slice thinly or mince finely based on heat preference", 
                          "cook": "add early for more heat or later for milder flavor"},
            "green chilli": {"prep": "remove stem, slice thinly or mince finely based on heat preference", 
                            "cook": "add early for more heat or later for milder flavor"},
            "bell pepper": {"prep": "remove seeds and stem, dice or slice as needed", 
                           "cook": "sauté until slightly softened but still crisp, about 3-4 minutes"},
            "cabbage": {"prep": "remove outer leaves, wash, and shred or chop as needed", 
                       "cook": "cook briefly until just wilted, about 3-5 minutes"},
            "spinach": {"prep": "wash thoroughly and remove tough stems if present", 
                       "cook": "wilt quickly in a hot pan, about 1-2 minutes only"},
            "garlic": {"prep": "peel and mince finely or crush in a garlic press", 
                      "cook": "sauté briefly until fragrant but not browned, about 30 seconds"},
            "ginger": {"prep": "peel and grate or mince finely", 
                      "cook": "sauté briefly until fragrant, about 30-60 seconds"},
            "mushroom": {"prep": "clean with a damp paper towel and slice or quarter", 
                        "cook": "sauté until golden and moisture has evaporated, about 5-7 minutes"},
            
            # Proteins
            "egg": {
                "prep": "crack into a bowl and whisk lightly for scrambled or fried eggs; keep whole for boiled eggs", 
                "cook": "scramble, fry, or boil according to recipe needs",
                "variants": {
                    "boiled egg": {"prep": "no preparation needed for whole eggs", 
                                 "cook": "place in cold water, bring to boil, and cook for 7-9 minutes for hard-boiled"},
                    "raw egg": {"prep": "crack into a bowl and whisk lightly", 
                              "cook": "use as binder in baked dishes or scramble until fully cooked"},
                    "poached egg": {"prep": "crack into a small bowl", 
                                  "cook": "slide into simmering water with a splash of vinegar and cook for 3-4 minutes"}
                }
            },
            "chicken": {"prep": "trim excess fat, cut into even pieces, and wash thoroughly", 
                       "cook": "cook thoroughly until no longer pink and internal temperature reaches 165°F/75°C"},
            "fish": {"prep": "clean, remove scales and bones if needed", 
                    "cook": "cook until it flakes easily with a fork and is opaque throughout"},
            "tofu": {"prep": "drain and press between paper towels to remove excess moisture", 
                    "cook": "pan-fry until golden on all sides, about 2-3 minutes per side"},
            "paneer": {"prep": "cut into even cubes or slices", 
                      "cook": "pan-fry until golden on all sides, about 2-3 minutes per side, or add directly to sauce"},
            
            # Fruits
            "apple": {"prep": "wash, core, and dice or slice as needed", 
                     "cook": "cook until softened but still holding shape, about 5-7 minutes"},
            "banana": {"prep": "peel and slice into rounds or lengthwise", 
                      "cook": "use raw or lightly fry for 1-2 minutes per side until caramelized"},
            "lemon": {"prep": "wash, zest if needed, and juice", 
                     "cook": "typically used raw for juice or zest"},
            
            # Dairy
            "cheese": {"prep": "grate, slice, or cube depending on recipe", 
                      "cook": "melt slowly over low heat or use as a topping"},
            "yogurt": {"prep": "stir well before using", 
                      "cook": "add at end of cooking and heat gently to prevent curdling"},
            "milk": {"prep": "measure out required amount", 
                    "cook": "heat gently over low heat, stirring frequently to prevent scorching"},
        }

    def welcome_message(self):
        """Display a welcome message explaining the program"""
        print("=" * 60)
        print("🍳 Welcome to the Advanced AI Recipe Generator! 🍳")
        print("=" * 60)
        print("Tell me what ingredients you have available, and I'll create")
        print("a unique personalized recipe just for you!")
        print("The AI will intelligently determine whether to create a main dish or snack")
        print("based on your ingredients.")
        print("=" * 60)

    def get_ingredients(self):
        """Get and process user ingredients input"""
        ingredients_input = input("\n👉 Enter your available ingredients (separated by commas): ")
        # Clean and format the ingredient list
        cleaned_ingredients = [item.strip().lower() for item in ingredients_input.split(",")]
        # Remove empty strings and capitalize first letter of each ingredient
        return [ingredient.capitalize() for ingredient in cleaned_ingredients if ingredient]

    def determine_recipe_type(self, ingredients):
        """Intelligently determine whether to create a main dish or snack based on ingredients"""
        # Convert ingredients to lowercase for matching
        lowercase_ingredients = [ing.lower() for ing in ingredients]
        
        # Count indicators for each type
        main_dish_count = 0
        snack_count = 0
        sweet_count = 0
        
        # Check if the ingredient list contains any ingredients that strongly indicate a dish type
        for ing in lowercase_ingredients:
            for indicator in self.main_dish_indicators:
                if indicator in ing:
                    main_dish_count += 1
                    
            for indicator in self.snack_indicators:
                if indicator in ing:
                    snack_count += 1
                    
            for indicator in self.sweet_indicators:
                if indicator in ing:
                    sweet_count += 1
        
        # Check for specific combinations that suggest a main dish
        has_protein = any(protein in " ".join(lowercase_ingredients) for protein in 
                         ["chicken", "beef", "fish", "pork", "tofu", "paneer", "shrimp", "mutton", "lamb"])
        
        has_starch = any(starch in " ".join(lowercase_ingredients) for starch in 
                        ["rice", "pasta", "potato", "noodle", "quinoa", "bread"])
        
        has_vegetable = any(veg in " ".join(lowercase_ingredients) for veg in 
                           ["carrot", "onion", "tomato", "spinach", "kale", "cabbage", "broccoli", 
                            "bell pepper", "capsicum", "eggplant", "zucchini"])
        
        # Analyze for egg specifics
        egg_keywords = ["egg", "eggs", "boiled egg", "raw egg", "poached egg"]
        has_egg = any(egg in " ".join(lowercase_ingredients) for egg in egg_keywords)
        # Specific type of eggs
        has_boiled_egg = any("boil" in ing and "egg" in ing for ing in lowercase_ingredients)
        
        # Make decision based on collected information
        if has_boiled_egg:
            # Boiled eggs are versatile, could be either main or snack
            # Consider other ingredients to decide
            if has_protein or has_starch or has_vegetable or len(ingredients) >= 4:
                return "main"
            else:
                return "snack"
        elif has_egg:
            # Raw eggs typically suggest main dishes (omelets, scrambled eggs, etc.)
            if has_protein or has_starch or has_vegetable:
                return "main"
            else:
                return "snack"  # Could be for something like egg salad
        elif has_protein and (has_starch or has_vegetable):
            # Classic main dish combination - protein with starch/vegetable
            return "main"
        elif main_dish_count > snack_count + sweet_count:
            return "main"
        elif snack_count > main_dish_count or sweet_count > main_dish_count:
            return "snack"
        elif len(ingredients) >= 5:
            # More ingredients typically suggests a main dish
            return "main"
        else:
            # Default to snack for small ingredient lists or ambiguous cases
            return "snack"

    def preprocess_ingredients(self, ingredients):
        """Preprocess ingredients to detect and handle special cases like egg types"""
        processed_ingredients = []
        
        for ingredient in ingredients:
            ingredient_lower = ingredient.lower()
            
            # Handle specific egg variants
            if "boiled egg" in ingredient_lower:
                processed_ingredients.append("Boiled egg")
                continue
            if "poached egg" in ingredient_lower:
                processed_ingredients.append("Poached egg")
                continue
            if "raw egg" in ingredient_lower or "egg" in ingredient_lower:
                # Just "egg" gets treated as raw egg for cooking purposes
                processed_ingredients.append("Egg")
                continue
                
            # Add original ingredient if no special handling needed
            processed_ingredients.append(ingredient)
            
        return processed_ingredients

    def get_preparation_method(self, ingredient):
        """Get the appropriate preparation method for a specific ingredient"""
        ingredient_lower = ingredient.lower()
        
        # Handle specific egg variants
        if "boiled egg" in ingredient_lower:
            return self.special_ingredients["egg"]["variants"]["boiled egg"]["prep"]
        if "poached egg" in ingredient_lower:
            return self.special_ingredients["egg"]["variants"]["poached egg"]["prep"]
        if "raw egg" in ingredient_lower or ingredient_lower == "egg":
            return self.special_ingredients["egg"]["variants"]["raw egg"]["prep"]
        
        # Check direct matches first with full ingredient name
        if ingredient_lower in self.special_ingredients:
            return self.special_ingredients[ingredient_lower]["prep"]
        
        # Check for partial matches when full name isn't found
        for special_ingredient, details in self.special_ingredients.items():
            if special_ingredient in ingredient_lower:
                return details["prep"]
        
        # Default preparation methods based on common categories as fallback
        if any(word in ingredient_lower for word in ["nut", "seed", "almond", "cashew", "walnut", "pista"]):
            return "use whole or lightly crush if preferred"
            
        if any(word in ingredient_lower for word in ["rice", "grain", "oat", "barley"]):
            return "rinse thoroughly before cooking"
            
        if any(word in ingredient_lower for word in ["lentil", "bean", "pea", "chickpea"]):
            return "rinse well and check for any debris"
            
        if any(word in ingredient_lower for word in ["cheese", "paneer"]):
            return "cut into appropriate sized cubes or grate as needed"
            
        if any(word in ingredient_lower for word in ["leafy", "spinach", "lettuce", "green"]):
            return "wash thoroughly and tear or chop as needed"
            
        # Default for most ingredients
        return "prepare as appropriate for the recipe"

    def get_cooking_method(self, ingredient):
        """Get the appropriate cooking method for a specific ingredient"""
        ingredient_lower = ingredient.lower()
        
        # Handle specific egg variants
        if "boiled egg" in ingredient_lower:
            return self.special_ingredients["egg"]["variants"]["boiled egg"]["cook"]
        if "poached egg" in ingredient_lower:
            return self.special_ingredients["egg"]["variants"]["poached egg"]["cook"]
        if "raw egg" in ingredient_lower or ingredient_lower == "egg":
            return self.special_ingredients["egg"]["variants"]["raw egg"]["cook"]
        
        # Check direct matches first with full ingredient name
        if ingredient_lower in self.special_ingredients:
            return self.special_ingredients[ingredient_lower]["cook"]
        
        # Check for partial matches when full name isn't found
        for special_ingredient, details in self.special_ingredients.items():
            if special_ingredient in ingredient_lower:
                return details["cook"]
        
        # Default cooking methods based on common categories as fallback
        if any(word in ingredient_lower for word in ["nut", "seed", "almond", "cashew"]):
            return "toast lightly in a dry pan until fragrant"
            
        if any(word in ingredient_lower for word in ["rice", "grain", "quinoa"]):
            return "cook according to package instructions until tender"
            
        if any(word in ingredient_lower for word in ["lentil", "bean", "chickpea"]):
            return "simmer until soft and fully cooked"
            
        if any(word in ingredient_lower for word in ["vegetable", "carrot", "potato"]):
            return "cook until tender but still retaining some texture"
            
        if any(word in ingredient_lower for word in ["meat", "chicken", "fish", "beef"]):
            return "cook thoroughly until safe internal temperature is reached"
            
        # Default for most ingredients
        return "cook until properly done"

    def create_coherent_snack_recipe(self, ingredients):
        """Create a coherent snack recipe that follows a logical sequence"""
        # Choose a snack style that fits the ingredients
        snack_method = random.choice(self.snack_methods)
        spice = random.choice(self.spices)
        herb = random.choice(self.herbs)
        
        # Identify main ingredients by type
        proteins = []
        veggies = []
        nuts_seeds = []
        boiled_eggs = []
        raw_eggs = []
        others = []
        
        # Categorize ingredients to create a coherent recipe
        for ingredient in ingredients:
            ingredient_lower = ingredient.lower()
            if "boiled egg" in ingredient_lower:
                boiled_eggs.append(ingredient)
            elif ingredient_lower == "egg" or "raw egg" in ingredient_lower:
                raw_eggs.append(ingredient)
            elif any(word in ingredient_lower for word in ["chicken", "fish", "meat", "tofu", "paneer"]):
                proteins.append(ingredient)
            elif any(word in ingredient_lower for word in ["onion", "tomato", "potato", "carrot", "chilli", "bell pepper", "cabbage", "spinach"]):
                veggies.append(ingredient)
            elif any(word in ingredient_lower for word in ["nut", "groundnut", "peanut", "almond", "seed", "sesame"]):
                nuts_seeds.append(ingredient)
            else:
                others.append(ingredient)
        
        # Combine eggs into proteins if appropriate
        if boiled_eggs:
            proteins = boiled_eggs + proteins
        if raw_eggs:
            proteins = raw_eggs + proteins
        
        # Determine snack type based on ingredients
        if boiled_eggs and veggies:
            recipe_name = f"{random.choice(self.snack_styles)} {boiled_eggs[0]} & {veggies[0]} Salad Bites"
            recipe_theme = f"protein-packed egg salad bites"
        elif raw_eggs and (nuts_seeds or veggies):
            if nuts_seeds:
                recipe_name = f"{random.choice(self.snack_styles)} {nuts_seeds[0]} & Egg Fritters"
                recipe_theme = f"savory egg and nut fritters"
            else:
                recipe_name = f"{random.choice(self.snack_styles)} {veggies[0]} & Egg Bites"
                recipe_theme = f"savory egg and vegetable bites"
        elif nuts_seeds and veggies:
            if proteins:
                recipe_name = f"{random.choice(self.snack_styles)} {nuts_seeds[0]} and {veggies[0]} Filled {proteins[0]} Bites"
                recipe_theme = f"savory {proteins[0]} bites with {nuts_seeds[0]} and vegetables"
            else:
                recipe_name = f"{random.choice(self.snack_styles)} {nuts_seeds[0]} & {veggies[0]} Crisps"
                recipe_theme = f"savory vegetable and nut crisps"
        elif proteins and veggies:
            recipe_name = f"{random.choice(self.snack_styles)} {proteins[0]} & {veggies[0]} Bites"
            recipe_theme = f"savory protein snack with vegetables"
        elif nuts_seeds:
            recipe_name = f"{random.choice(self.snack_styles)} {nuts_seeds[0]} Munch"
            recipe_theme = f"spiced nut snack"
        elif proteins:
            recipe_name = f"{random.choice(self.snack_styles)} {proteins[0]} Snack Bites" 
            recipe_theme = f"high-protein snack bites"
        else:
            recipe_name = f"{random.choice(self.snack_styles)} {ingredients[0]} {random.choice(self.snack_types)}"
            recipe_theme = f"simple snack featuring {ingredients[0]}"
        
        # Create logical preparation steps
        preparation_steps = []
        for ingredient in ingredients:
            prep_method = self.get_preparation_method(ingredient)
            preparation_steps.append(f"{ingredient}: {prep_method}")
        
        # Generate sensible, sequenced cooking instructions
        cooking_steps = []
        
        # Determine if the snack is a baked, fried, or no-cook snack
        is_baked = snack_method in ["bake", "roast"]
        is_fried = snack_method in ["fry"]
        is_no_cook = snack_method in ["chill", "mix", "assemble"]
        
        # Check if we have eggs (and what type)
        has_boiled_egg = any("boiled egg" in ingredient.lower() for ingredient in ingredients)
        has_raw_egg = any((ingredient.lower() == "egg" or "raw egg" in ingredient.lower()) for ingredient in ingredients)
        
        # Implement logical cooking steps based on recipe type and ingredients
        if is_baked:
            temp = random.randint(160, 200)
            cooking_steps.append(f"Preheat your oven to {temp}°C.")
            
            # Handle boiled eggs if present
            if has_boiled_egg:
                cooking_steps.append(f"Peel and chop the boiled eggs into small pieces.")
            
            # Handle nuts first if present
            for nut in nuts_seeds:
                cooking_steps.append(f"Spread {nut} on a baking sheet and {self.get_cooking_method(nut).split(',')[0]}.")
            
            # Mix ingredients or prepare vegetables
            if veggies:
                veggie_text = ", ".join(veggies)
                cooking_steps.append(f"Prepare {veggie_text} according to the preparation instructions.")
                
            # Handle egg binding if present
            if has_raw_egg:
                cooking_steps.append("Beat the egg in a bowl.")
                cooking_steps.append(f"Mix all other prepared ingredients with the beaten egg and {spice}.")
            else:
                cooking_steps.append(f"Mix all prepared ingredients together with a pinch of {spice}.")
                
            cooking_steps.append(f"Form the mixture into small balls or patties and place on a baking sheet lined with parchment paper.")
            cooking_steps.append(f"Bake for 15-20 minutes until golden and cooked through.")
            
        elif is_fried:
            # Mix ingredients
            if has_boiled_egg:
                cooking_steps.append(f"Mash the peeled boiled eggs in a bowl.")
                cooking_steps.append(f"Mix with the other prepared ingredients and {spice}.")
            elif has_raw_egg:
                cooking_steps.append("Beat the egg in a bowl.")
                cooking_steps.append(f"Mix all other prepared ingredients with the beaten egg and {spice}.")
                cooking_steps.append("Form the mixture into small patties or balls.")
            else:
                cooking_steps.append(f"Mix all prepared ingredients together with a pinch of {spice}.")
                cooking_steps.append("Form into patties or small balls if possible.")
                
            cooking_steps.append("Heat oil in a pan over medium heat.")
            cooking_steps.append("Carefully add the formed patties/balls to the hot oil.")
            cooking_steps.append("Fry for 2-3 minutes on each side until golden brown and cooked through.")
            cooking_steps.append("Remove and drain on paper towels to remove excess oil.")
            
        elif is_no_cook:
            # Handle boiled eggs if present
            if has_boiled_egg:
                cooking_steps.append(f"Peel and chop the boiled eggs into small pieces.")
                
            # Process nuts first
            for nut in nuts_seeds:
                cooking_steps.append(f"{self.get_cooking_method(nut).split(',')[0]}.")
                
            cooking_steps.append(f"In a mixing bowl, combine all prepared ingredients.")
            cooking_steps.append(f"Add a pinch of {spice} and mix well.")
            
            if snack_method == "chill":
                cooking_steps.append("Cover the bowl and refrigerate for at least 30 minutes to allow flavors to meld.")
                
        else:  # Default steps for other methods
            # Handle boiled eggs if present
            if has_boiled_egg:
                cooking_steps.append(f"Peel and chop the boiled eggs into small pieces.")
                
            # Handle raw eggs
            if has_raw_egg and not has_boiled_egg:
                if snack_method in ["scramble", "cook"]:
                    cooking_steps.append("Beat the eggs in a bowl with a pinch of salt.")
                    cooking_steps.append("Heat a non-stick pan over medium heat.")
                    cooking_steps.append("Pour in the beaten eggs and gently scramble until just set.")
                    cooking_steps.append("Set aside to cool slightly before mixing with other ingredients.")
                else:
                    cooking_steps.append("Beat the eggs in a bowl.")
                    cooking_steps.append("Use as a binding agent when mixing with other ingredients.")
                
            cooking_steps.append(f"In a bowl, combine all prepared ingredients with a pinch of {spice}.")
            cooking_steps.append(f"{snack_method.capitalize()} according to your preferred technique until properly prepared.")
        
        # Final step for all recipes
        cooking_steps.append(f"Garnish with fresh {herb} before serving.")
        
        # Generate serving suggestions
        serving_suggestions = [
            f"Serve as a snack on its own or with a dipping sauce of your choice.",
            f"This {recipe_theme} is perfect for party appetizers or a quick snack.",
            f"Store in an airtight container and consume within 2-3 days for best flavor."
        ]
        
        # Determine total time
        if is_baked:
            total_time = "25-30 minutes (including baking time)"
        elif is_fried:
            total_time = "15-20 minutes"
        else:
            total_time = "10-15 minutes" if not is_no_cook else "5-10 minutes (plus chilling time if desired)"
        
        # Structure the full recipe
        recipe = {
            "name": recipe_name,
            "ingredients": ingredients + [spice, f"Fresh {herb}", "Salt to taste"],
            "preparation": preparation_steps,
            "cooking": cooking_steps,
            "serving": serving_suggestions,
            "tips": [
                f"You can adjust the spice level to your preference by adding more or less {spice}.",
                f"Total preparation and cooking time: {total_time}."
            ]
        }
        
        return recipe

    def create_coherent_main_dish(self, ingredients):
        """Create a coherent main dish recipe that follows a logical cooking sequence"""
        # Choose cooking elements
        method = random.choice(self.cooking_methods)
        spices = random.sample(self.spices, min(3, len(self.spices)))
        herb = random.choice(self.herbs)
        oil = random.choice(self.oils)
        
        # Categorize ingredients for logical cooking sequence
        aromatics = []  # onions, garlic, ginger, etc.
        proteins = []   # meat, fish, tofu, paneer, eggs
        veggies = []    # most vegetables
        starches = []   # potatoes, rice, etc.
        garnishes = []  # herbs, nuts, etc.
        boiled_eggs = []  # specifically boiled eggs
        raw_eggs = []     # raw eggs
        
        for ingredient in ingredients:
            ingredient_lower = ingredient.lower()
            if "boiled egg" in ingredient_lower:
                boiled_eggs.append(ingredient)
            elif ingredient_lower == "egg" or "raw egg" in ingredient_lower:
                raw_eggs.append(ingredient)
            elif any(item in ingredient_lower for item in ["onion", "garlic", "ginger", "chilli"]):
                aromatics.append(ingredient)
            elif any(item in ingredient_lower for item in ["chicken", "fish", "meat", "beef", "pork", "tofu", "paneer"]):
                proteins.append(ingredient)
            elif any(item in ingredient_lower for item in ["potato", "rice", "pasta", "noodle", "quinoa"]):
                starches.append(ingredient)
            elif any(item in ingredient_lower for item in ["herb", "seed", "nut", "groundnut", "peanut"]):
                garnishes.append(ingredient)
            else:
                veggies.append(ingredient)  # default category
        # End of ingredient categorization from previous code
        
        # Generate recipe name based on ingredients
        style = random.choice(self.cooking_styles)
        dish_type = random.choice(self.dish_types)
        
        if proteins:
            main_ingredient = proteins[0]
        elif starches:
            main_ingredient = starches[0]
        elif veggies:
            main_ingredient = veggies[0]
        elif boiled_eggs:
            main_ingredient = boiled_eggs[0]
        elif raw_eggs:
            main_ingredient = "Egg"
        else:
            main_ingredient = ingredients[0]
            
        # Create recipe name with two main ingredients if available
        if len(ingredients) > 1:
            second_ingredient = None
            if main_ingredient in proteins and veggies:
                second_ingredient = veggies[0]
            elif main_ingredient in proteins and starches:
                second_ingredient = starches[0]
            elif main_ingredient in starches and veggies:
                second_ingredient = veggies[0]
            elif main_ingredient in veggies and (proteins or starches):
                second_ingredient = (proteins or starches)[0]
            elif main_ingredient in boiled_eggs and veggies:
                second_ingredient = veggies[0]
            elif main_ingredient in raw_eggs and veggies:
                second_ingredient = veggies[0]
            
            if second_ingredient and second_ingredient != main_ingredient:
                recipe_name = f"{style} {main_ingredient} & {second_ingredient} {dish_type}"
            else:
                recipe_name = f"{style} {main_ingredient} {dish_type}"
        else:
            recipe_name = f"{style} {main_ingredient} {dish_type}"
        
        # Create preparation steps
        preparation_steps = []
        
        # Handle each ingredient's preparation
        for ingredient in ingredients:
            prep_method = self.get_preparation_method(ingredient)
            preparation_steps.append(f"{ingredient}: {prep_method}")
        
        # Generate cooking steps
        cooking_steps = []
        
        # Start with heating oil
        cooking_steps.append(f"Heat {oil} in a pan over medium heat.")
        
        # Cook aromatics first if present
        if aromatics:
            aromatics_text = " and ".join(aromatics)
            cooking_steps.append(f"Add {aromatics_text} and sauté until fragrant, about 1-2 minutes.")
        
        # Cook proteins next if present
        if proteins:
            proteins_text = " and ".join(proteins)
            cooking_steps.append(f"Add {proteins_text} and {method} until properly cooked.")
            
            # Add specific protein cooking instructions if applicable
            for protein in proteins:
                if protein.lower() in self.special_ingredients:
                    protein_cooking = self.get_cooking_method(protein)
                    cooking_steps.append(f"Ensure {protein} is {protein_cooking}")
            
        # Add spices
        spice_text = ", ".join(spices)
        cooking_steps.append(f"Add {spice_text} and salt to taste, stir well to combine.")
        
        # Add vegetables next
        if veggies:
            veggies_text = " and ".join(veggies)
            cooking_steps.append(f"Add {veggies_text} and cook until vegetables are tender but still retain some texture.")
        
        # Add starches if present
        if starches:
            starches_text = " and ".join(starches)
            cooking_steps.append(f"Add {starches_text} and cook according to their required cooking time.")
        
        # Add raw eggs if present
        if raw_eggs:
            cooking_steps.append("Beat the eggs in a bowl.")
            cooking_steps.append("Pour the beaten eggs into the pan and gently stir until eggs are cooked.")
        
        # Add boiled eggs if present
        if boiled_eggs:
            cooking_steps.append("Slice the boiled eggs and add them to the dish.")
        
        # Finishing touches
        cooking_steps.append(f"Garnish with fresh {herb} before serving.")
        
        # Generate serving suggestions
        serving_suggestions = [
            f"Serve hot with your choice of bread or rice.",
            f"This {recipe_name} pairs well with a fresh green salad.",
            f"Leftovers can be refrigerated for up to 2 days. Reheat thoroughly before serving."
        ]
        
        # Determine total preparation and cooking time
        prep_time = 10 if len(ingredients) <= 5 else 15
        cook_time = 15 if len(ingredients) <= 5 else 25
        
        # Structure the full recipe
        recipe = {
            "name": recipe_name,
            "ingredients": ingredients + spices + [f"Fresh {herb}", oil, "Salt to taste"],
            "preparation": preparation_steps,
            "cooking": cooking_steps,
            "serving": serving_suggestions,
            "tips": [
                f"You can adjust the spice level to your preference by adding more or less {spices[0]}.",
                f"Total preparation time: {prep_time} minutes. Cooking time: {cook_time} minutes."
            ]
        }
        
        return recipe

    def format_recipe(self, recipe):
        """Format and print the recipe in a user-friendly way"""
        # Header
        print("\n" + "=" * 60)
        print(f"🍽️  {recipe['name'].upper()}  🍽️")
        print("=" * 60)
        
        # Ingredients
        print("\n📋 INGREDIENTS:")
        for ingredient in recipe['ingredients']:
            print(f"  • {ingredient}")
        
        # Preparation
        print("\n🔪 PREPARATION:")
        for i, step in enumerate(recipe['preparation'], 1):
            print(f"  {i}. {step}")
        
        # Cooking
        print("\n🍳 COOKING INSTRUCTIONS:")
        for i, step in enumerate(recipe['cooking'], 1):
            print(f"  {i}. {step}")
        
        # Serving
        print("\n🍽️ SERVING SUGGESTIONS:")
        for suggestion in recipe['serving']:
            print(f"  • {suggestion}")
        
        # Tips
        print("\n💡 TIPS:")
        for tip in recipe['tips']:
            print(f"  • {tip}")
        
        print("\n" + "=" * 60)
        print("Enjoy your delicious meal! 😋")
        print("=" * 60)

    def run(self):
        """Main function to run the recipe generator"""
        self.welcome_message()
        ingredients = self.get_ingredients()
        
        if not ingredients:
            print("⚠️ No ingredients provided. Please try again with at least one ingredient.")
            return
        
        print(f"\n✅ Ingredients received: {', '.join(ingredients)}")
        
        # Preprocess ingredients for special handling
        processed_ingredients = self.preprocess_ingredients(ingredients)
        
        # Always generate 3 recipes automatically
        num_recipes = 3
        print(f"\n🔍 Generating {num_recipes} unique recipe options based on your ingredients...")
        
        # Generate multiple recipes
        recipes = []
        
        # First recipe - based on ingredient analysis
        recipe_type = self.determine_recipe_type(processed_ingredients)
        print(f"\n🍳 Creating recipe option #1 ({recipe_type})...")
        if recipe_type == "snack":
            recipes.append(self.create_coherent_snack_recipe(processed_ingredients))
        else:
            recipes.append(self.create_coherent_main_dish(processed_ingredients))
        
        # Second recipe - opposite of first recipe type
        recipe_type = "main" if recipe_type == "snack" else "snack"
        print(f"\n🍳 Creating recipe option #2 ({recipe_type})...")
        if recipe_type == "snack":
            recipes.append(self.create_coherent_snack_recipe(processed_ingredients))
        else:
            recipes.append(self.create_coherent_main_dish(processed_ingredients))
        
        # Third recipe - same as first type but with variations
        recipe_type = "main" if recipes[0] == "snack" else "main"
        print(f"\n🍳 Creating recipe option #3 ({recipe_type})...")
        if recipe_type == "snack":
            recipes.append(self.create_coherent_snack_recipe(processed_ingredients))
        else:
            recipes.append(self.create_coherent_main_dish(processed_ingredients))
        
        # Display all recipes with option numbers
        print("\n" + "=" * 60)
        print("🍽️  YOUR RECIPE OPTIONS  🍽️")
        print("=" * 60)
        
        for i, recipe in enumerate(recipes, 1):
            print(f"\n{i}. {recipe['name']}")
        
        # Let user choose which recipe to view in detail
        while True:
            try:
                selection = int(input(f"\n👉 Which recipe would you like to view in detail (1-{num_recipes})? "))
                if 1 <= selection <= num_recipes:
                    # Format and display the selected recipe
                    self.format_recipe(recipes[selection-1])
                    break
                else:
                    print(f"Please enter a number between 1 and {num_recipes}.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Ask if they want to generate new recipes
        another_choice = input("\nWould you like to generate new recipes with different ingredients? (y/n): ").lower()
        if another_choice == 'y':
            self.run()
        else:
            print("\nThank you for using the AI Recipe Generator! Bon appétit! 👨‍🍳")


# Run the program if this script is executed directly
if __name__ == "__main__":
    generator = RecipeGenerator()
    generator.run()