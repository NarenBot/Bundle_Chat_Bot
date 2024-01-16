## ::: Base Skeleton for Data-Science Projects :::

### Steps to run this Bare-Bones Template: 
**{Note}**: Operates exclusively within the 'Git Bash' environment.

1. Run below command 
```bash
python template.py
```
-|- Upon initiating the project, remove the 'temp.log' temporary log file.

-|- Include modules or packages in the requirements.txt file according to the specific requirements of your project.

-|- Modify the 'setup.cfg' and 'setup.py' files according to the specific requirements(project_name_description) of the project.

2. Run below command
```bash
bash init_setup.sh
```

**To activate environment in bash:**
```bash
source ~/Anaconda3/etc/profile.d/conda.sh
conda activate venv/
```

3. Run below command (optional)
```bash
pytest -v
tox
```

### Steps to deploy the package to PyPI:
 - Create an account on PyPI and obtain the API token.
 - Add the acquired token to the GitHub secrets for secure storage.
 - In the setup.py file, introduce two parameters: long_description and long_description_content_type then comment out the line corresponding to the "install_requires" parameter.
 - Initialize the release on GitHub.
 - Include a python-publish.yml file and publish it.

<br>

### Steps to follow proof-of-concept (POC) project:
   - Run the command: "python template.py"
   - Please eliminate the following - tests folder, pyproject.toml, README.md, requirements_dev.txt, setup.cfg, temp.log, template.py and tox.ini files.
   - Add LONG_DESCRIPTION in README.md, PROJECT_NAME in setup.py and PACKAGES in requirements.txt file.
   - In setup.py file change value as "." on "package_dir" parameter.
   - Run the command: "bash init_setup.sh" and Activate the environment.

---

The base skeleton for a data science project typically includes the following components:

1. **Project Structure:**
   - Create a well-organized directory structure for your project.
   - Divide folders for data, code, documentation, and models.

2. **Data Collection and Exploration:**
   - Gather relevant data from various sources.
   - Explore and understand the data through descriptive statistics and visualizations.

3. **Data Cleaning and Preprocessing:**
   - Handle missing values, outliers, and inconsistencies in the data.
   - Transform and preprocess the data for analysis.

4. **Feature Engineering:**
   - Create new features or transform existing ones to improve model performance.

5. **Model Building:**
   - Select appropriate algorithms based on the problem.
   - Split the data into training and testing sets.
   - Train and evaluate models using appropriate metrics.

6. **Model Deployment:**
   - Deploy the chosen model for real-world use if applicable.

7. **Documentation:**
   - Provide clear documentation for your code, including comments and a README file.

8. **Version Control:**
   - Use version control (e.g., Git) to track changes and collaborate with others.

9. **Testing and Validation:**
   - Implement testing procedures to validate the correctness of your code.

10. **Visualization and Reporting:**
    - Create visualizations to communicate insights.
    - Prepare a report summarizing the findings and methodology.

This basic structure ensures a systematic and reproducible approach to data science projects.