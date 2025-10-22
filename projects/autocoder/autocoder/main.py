def process_goal(goal, max_retries=3):
    for attempt in range(1, max_retries+1):
        log(f"Goal: {goal} (Attempt {attempt}/{max_retries})")
        code = generate_code(goal)
        if not code or code.startswith("Claude error:"):
            log(code if code else "Empty generation.")
            continue

        # —— SYNTAX CHECK —— 
        try:
            ast.parse(code)
        except SyntaxError as e:
            log(f"SyntaxError: {e}")
            # ask Claude to fix the syntax
            goal = f"Fix the syntax error:\n{e}\nOriginal goal: {goal}"
            continue

        path = write_code_file(goal, code)
        out, err = execute_file(path)
        if err:
            log(f"Error: {err}")
            goal = f"Fix the error:\n{err}\nOriginal goal: {goal}"
            continue

        log(f"Output: {out or '(no output)'}")
        return True

    log("Max retries reached.")
    return False
def main():
    while True:
        try:
            goal = input("\nEnter goal (or 'exit'): ").strip()
            if goal.lower() == "exit":
                break
            if goal:
                process_goal(goal)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
