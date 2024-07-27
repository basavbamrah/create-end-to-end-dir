# ML-DS-DL Project Directory Structure Generator
This Python script helps you create a well-organized directory structure for your ML, DL, or LLM projects. It provides a foundation for project development and promotes maintainability.

## Usage
Clone the repository and run the following command

**To create the default structure (src, notebooks, app):**
```
    python create_project_structure.py
```

**To create specific directories:**

```
python create_project_structure.py --create-dirs data models scripts
```

Replace data, models, scripts with the directories you want to create. You can specify multiple directories.

## Customization
The script allows you to customize the directory structure by providing a list of directories to create using the --create-dirs argument.

**Example:**

```
python create_project_structure.py --create-dirs data/processed models/checkpoints reports
```

This will create the following directories:

data/processed
models/checkpoints
reports
Directory Structure
The script creates the following directory structure by default:

```
    project_root/
    ├── data/
    │   ├── raw/
    │   ├── processed/
    │   ├── external/
    │   └── interim/
    ├── notebooks/
    │   ├── exploratory/
    │   ├── modeling/
    │   └── presentation/
    ├── src/
    │   ├── data/
    │   ├── features/
    │   ├── models/
    │   ├── utils/
    │   ├── app/
    │   └── pipelines/
    ├── tests/
    ├── scripts/
    ├── config/
    ├── models/
    │   ├── trained_models/
    │   ├── checkpoints/
    │   └── artifacts/
    ├── reports/
    │   ├── experiment_reports/
    │   └── model_cards/
    ├── docs/
    └── .gitignore
```

Note: You can modify the default list of directories in the script (create_directory_structure.py) to suit your specific project needs.

## Additional Notes
This script creates directories and does not populate them with files. You can customize the structure further by adding your own files and subfolders.
Consider using version control (e.g., Git) to track changes to your project structure.
Feel free to adapt and extend this script based on your workflow and project requirements. By using this tool and maintaining a well-organized structure, you can improve the maintainability and collaboration around your ML projects.
