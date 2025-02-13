Design: OrganizationApp
Classes:
    OrganizationApp:
        Manages the main execution loop.
        Reads and processes user commands.
        Parses and validates input.
        Initiates and runs the engine.

    Engine (Executes Commands):
        Manages the worker database.
        Creates Employee objects.
        Handles adding, removing, and assigning employees.

    Employee (Parent Class of Worker and CEO):
        Supports database search and navigation.
        Performs updates to the database.

    Worker:
        Represents all employees except the CEO.

Database Architecture:

    Organization Tree:
        The CEO sits at the top, with all employees below.
        Each worker maintains a list of subordinates.
        Departments exist directly below the CEO.

    Organization Departments:
        Each department is positioned one level beneath the CEO.
        Contains a list of workers, where the first worker is the department director.