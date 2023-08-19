/**
 * A function to add two numbers.
 * @param {number} num1 - The first number.
 * @param {number} num2 - The second number.
 * @returns {number} - The sum of num1 and num2.
 */
function addNumbers(num1, num2) {
    return num1 + num2;
}

/**
 * A simple test function for addNumbers.
 */
function testAddNumbers() {
    const test1 = addNumbers(3, 4);
    const test2 = addNumbers(-1, 5);
    const test3 = addNumbers(0, 0);

    console.log(`Test 1 (3 + 4): Expected 7, Got ${test1}`);
    console.log(`Test 2 (-1 + 5): Expected 4, Got ${test2}`);
    console.log(`Test 3 (0 + 0): Expected 0, Got ${test3}`);
}

// Run the test function
testAddNumbers();
