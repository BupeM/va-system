#VERBAL AUTOPSY SYSTEM
A verbal autopsy is a method used to determine the probable cause of death of an individual in the case where a doctor or a medical professional is not available. It uses a structured questionnaire to find out about the symptoms and events that occured before the persion died to help determine what might have caused the death.




#HOW TO RUN
1. Clone the repository:
```bash
git clone git@github.com:BupeM/va-system.git

2. Navigate into the project
cd va_system #the project name has an underscroll while the repo has a hyphen.

3. Create and activate a vertual environment
python3.14 -m venv .venv
source .venv/bin/activate

4. Install the required dependencies
pip install -r requirements.txt

5. Run the database migrations
python manage.py migrate

6. Start the development server
python manage.py runserver




#URL DEPLOYMENT:
https://edpythonaw.pythonanywhere.com/home/




#WHAT I LEARNED
> What a verbal autopsy is and how it is useful in some circumstances.
> The fundamentals of django MVT and how the compondents run together.
>The importance of migration files to keep the database structure consistent.
>How to deploy a web application.


BUPE MWABA