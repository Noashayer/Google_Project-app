import google.generativeai as genai
import os
from dotenv import load_dotenv

def setup_gemini():
    """Set up and configure the Gemini API client."""
    # Load API key from .env file
    load_dotenv()
    
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key or set it directly.")
        return False
        
    # Configure the Gemini API with your key
    genai.configure(api_key=api_key)
    return True

def list_available_models():
    """List all available models from Google Generative AI."""
    try:
        models = genai.list_models()
        print("Available models:")
        gemini_models = []
        for model in models:
            if "gemini" in model.name.lower():
                print(f"- {model.name}")
                gemini_models.append(model.name)
        return gemini_models
    except Exception as e:
        print(f"Error listing models: {str(e)}")
        return []

def test_model(model_name):
    """Test if a model works by sending a simple query."""
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello, can you respond with a simple 'yes' if you can hear me?")
        return True
    except Exception as e:
        print(f"Model {model_name} test failed: {str(e)}")
        return False

def get_gemini_response(prompt, model_name):
    """Get a response from Gemini for a given prompt."""
    try:
        # Initialize the model
        model = genai.GenerativeModel(model_name)
        
        # Generate content
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini: {str(e)}"

def find_working_model(gemini_models):
    """Find a working model from the list of available models."""
    print("Testing available models to find one that works...")
    
    # First try preferred models in order
    preferred_models = ["gemini-pro", "gemini-1.5-pro", "gemini-1.0-pro"]
    for preferred in preferred_models:
        for model in gemini_models:
            if preferred in model:
                print(f"Testing model: {model}")
                if test_model(model):
                    print(f"Found working model: {model}")
                    return model
    
    # If preferred models don't work, try all available models
    for model in gemini_models:
        if model not in [m for p in preferred_models for m in gemini_models if p in m]:
            print(f"Testing model: {model}")
            if test_model(model):
                print(f"Found working model: {model}")
                return model
    
    return None

def create_prompt(subject, grade, topic, level):
    """Create a prompt for Gemini based on student information."""
    prompt = f"""חפש בגוגל שאלה מתאימה לפי המקצוע-{subject}, הכיתה- {grade}, נושא- {topic}, והקבצה- {level} של התלמיד. 
    הבא שאלה אמיתית, נכונה, וברורה, שמותאמת לשכבת הגיל שלו
    יש להחזיר תשובה נקייה וברורה, תחפש בגוגל ותשלח קישור למה שמצאת לפחות חמש שאלות
    אם אין משהו שבדיוק לחומר עדיין תשלח"""
    return prompt

def main():
    """Main function to run the Gemini question-answering program."""
    print("ברוכים הבאים למערכת שאלות לימודיות!")
    print("--------------------------------------------")
    
    # Set up the API
    if not setup_gemini():
        return
    
    print("מאתר מודל גמיני שעובד...")
    
    # List available models at startup
    gemini_models = list_available_models()
    if not gemini_models:
        print("לא נמצאו מודלים של גמיני. אנא בדוק את מפתח ה-API שלך.")
        return
    
    # Find a working model before asking user questions
    working_model = find_working_model(gemini_models)
    
    if not working_model:
        print("לא נמצאו מודלים עובדים. אנא בדוק את חיבור האינטרנט ומפתח ה-API שלך.")
        return
    
    print(f"\nמשתמש במודל: {working_model}")
    print("אנא הזן את הפרטים הבאים כדי לקבל שאלות מותאמות.")
    print("הקלד 'יציאה' או 'סיום' כדי לסיים את התוכנית.")
    
    while True:
        # Get student information
        print("\nאנא הזן את הפרטים הבאים:")
        subject = input("מקצוע (למשל: מתמטיקה): ")
        
        # Check if user wants to exit
        if subject.lower() in ["יציאה", "סיום", "exit", "quit"]:
            print("תודה שהשתמשת במערכת. להתראות!")
            break
        
        grade = input("כיתה (למשל: ט): ")
        topic = input("נושא לימודי (למשל: חפיפת משולשים): ")
        level = input("הקבצה (למשל: א): ")
        
        # Create the prompt
        prompt = create_prompt(subject, grade, topic, level)
        
        # Get and display the response
        print(f"\nמחפש שאלות מתאימות...")
        response = get_gemini_response(prompt, working_model)
          
        # If there's an error, try to find another working model
        if "Error communicating with Gemini" in response:
            print("שגיאה במודל הנוכחי, מחפש מודל אחר שעובד...")
            gemini_models.remove(working_model)  # Remove the failed model
            
            if not gemini_models:
                print("אין עוד מודלים זמינים לניסיון.")
                break
                
            working_model = find_working_model(gemini_models)
            if not working_model:
                print("לא נמצאו מודלים עובדים. אנא בדוק את חיבור האינטרנט שלך.")
                break
                
            print(f"עבר למודל: {working_model}")
            # Try the question again with the new model
            response = get_gemini_response(prompt, working_model)
        
        print("\nהשאלות המומלצות:")
        print(response)
        
        # Ask if the user wants to continue
        continue_choice = input("\nהאם תרצה לחפש שאלות נוספות? (כן/לא): ")
        if continue_choice.lower() not in ["כן", "yes", "y"]:
            print("תודה שהשתמשת במערכת. להתראות!")
            break

if _name_ == "_main_":
    main()
