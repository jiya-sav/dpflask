

const generateRecipeLinkButton = document.querySelector("#generate-recipe-link-button");
const ingredientsTextbox = document.querySelector("#ingredients-textbox");
const prepTimeTextbox = document.querySelector("#prep-time-textbox");
const API_KEY = "8f0cc3fa5a68443591601bf8122d830e";
 
generateRecipeLinkButton.addEventListener("click", async () => {
	const ingredients = ingredientsTextbox.value.split(",").map(ingredient => ingredient.trim());
	const prepTime = prepTimeTextbox.value;
 
	// calling api w the ingredients and preptime the user inputted
	const response = await fetch(`https://api.spoonacular.com/recipes/complexSearch?apiKey=${API_KEY}&ingredients=${ingredients.join(",")}&maxReadyTime=${prepTime}`);
	const searchResults = await response.json();
	const recipe = searchResults.results[0];
		
	// show recipe link !!!
	const recipeLink = document.querySelector("#recipe-link");
	recipeLink.textContent = recipe.title;
	recipeLink.href = `https://spoonacular.com/recipes/${recipe.title.replace(/\s/g, "-").toLowerCase()}-${recipe.id}`;
	});
 
 
 
 