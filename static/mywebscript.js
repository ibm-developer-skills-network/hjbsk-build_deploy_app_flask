    const sendRequest = async (operation) => {
    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;

    try {
        const response = await fetch(`${operation}?num1=${num1}&num2=${num2}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.text();
        document.getElementById("system_response").innerHTML = data;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById("system_response").innerHTML = 'An error occurred, please try again.';
    }
};

const runOperation = (operation) => {
      sendRequest(operation);
};

const runAddition = () => runOperation("sum");
const runSubtraction = () => runOperation("sub");
const runMultiplication = () => runOperation("mul");
