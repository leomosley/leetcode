function isValid(s: string): boolean {
    const stack: string[] = [];
    const brackets = { ')': '(', '}': '{', ']': '[' }

    for (const char of s) {
        if (brackets[char]) {
            if (!stack || stack[stack.length - 1] !== brackets[char]) {
                return false
            }
            stack.pop()
        } else {
            stack.push(char)
        }
    }

    return stack.length === 0;
};