## Step to run restaurant-genai
- Clone restaurant-genai in your local machine
- Download and install Anaconda from https://www.anaconda.com/download
- Type anaconda on windows search and open anaconda command prompt
- Navigate to restaurant-genai progect (in step 1) from conda prompt and/by follow below commands
    * cd <basepath>/restaurant-genai
    * conda create -n restaurant-genai python=3.11 -y
    * conda activate restaurant-genai
    * pip install -r requirement.txt
- Create a file with name '.env' in restaurant-genai folder
- Add below line in .env file
    * OPENAI_API_KEY="Supply your secret token here"
- Run Multiple PDF File Reader with below command
    * streamlit run src\app.py --server.port 8080
- Open http://localhost:8080/ on your favorite browser
    * Share any website link on side bar and ask any question within the context of the website
