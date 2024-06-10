
//for the date//
window.onload = function () {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

    today = mm + '/' + dd + '/' + yyyy;
    document.querySelector('.date').textContent += ' ' + today;
};


function addRow() {
    // Get the table element
    var table = document.getElementById("origin_Table");

    // Find the last row index
    var lastRowIndex = table.rows.length - 3; // Adjust based on the structure

    // Find the last existing row number
    var lastExistingRowNumber = lastRowIndex > 1 ? parseInt(table.rows[lastRowIndex - 1].cells[0].textContent) : 0;

    // Create a new row after the last existing row
    var newRow = table.insertRow(lastRowIndex);

    // Create cells in the new row
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);
    var cell6 = newRow.insertCell(5);
    var cell7 = newRow.insertCell(6);
    

    // Set content for the cells
    cell1.textContent = lastExistingRowNumber + 1; // Counting continues
    cell2.appendChild(createInputWithAutocomplete());
    cell3.contentEditable = true;
    cell4.contentEditable = true;
    cell5.contentEditable = true;
    cell6.textContent = "";
    cell7.appendChild(createSelectWithOptions());

    // Add other logic as needed for customization
}

function removeRow() {
    var table = document.getElementById("origin_Table");
    var lastRowIndex = table.rows.length - 3; // Adjust based on the structure

    if (lastRowIndex > 1) {
        table.deleteRow(lastRowIndex - 1);
    } else {
        alert("Cannot remove the last row!");
    }
}

// ---------------------addRow_destination_table---------------------- //
function addRow_destination_table() {
    // Get the table element
    var table = document.getElementById("destination_table");

    // Find the last row index
    var lastRowIndex = table.rows.length -1; // Adjust based on the structure

    // Find the last existing row number
    var lastExistingRowNumber = lastRowIndex > 1 ? parseInt(table.rows[lastRowIndex - 1].cells[0].textContent) : 0;

    // Create a new row after the last existing row
    var newRow = table.insertRow(lastRowIndex);

    // Create cells in the new row
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);
    var cell6 = newRow.insertCell(5);
    var cell7 = newRow.insertCell(6);
    

    // Set content for the cells
    cell1.textContent = lastExistingRowNumber + 1; // Counting continues
    cell2.appendChild(createInputWithAutocomplete());
    cell3.contentEditable = true;
    cell4.contentEditable = true;
    cell5.contentEditable = true;
    cell6.textContent = "";
    cell7.appendChild(createSelectWithOptions());

    // Add other logic as needed for customization
}

function removeRow_destination_table() {
    var table = document.getElementById("destination_table");
    var lastRowIndex = table.rows.length - 1; // Adjust based on the structure

    if (lastRowIndex > 1) {
        table.deleteRow(lastRowIndex - 1);
    } else {
        alert("Cannot remove the last row!");
    }
}

// ---------------------addRow_destination_table---------------------- //

function createInputWithAutocomplete() {
    // Create input element
    var input = document.createElement("input");

    // Set attributes for input
    input.setAttribute("type", "text");
    input.setAttribute("id", "autocompleteInput");
    input.setAttribute("placeholder", "Type to search");


    // Create ul element for autocomplete dropdown list
    var autocompleteList = document.createElement("ul");
    autocompleteList.setAttribute("id", "autocompleteList");

    // Append the ul element to the input container
    var autocompleteContainer = document.createElement("div");
    autocompleteContainer.setAttribute("id", "autocompleteContainer");
    autocompleteContainer.appendChild(input);
    autocompleteContainer.appendChild(autocompleteList);

    // Add event listener for input changes
    input.addEventListener("input", function () {
        var inputValue = input.value.toUpperCase();
        autocompleteList.innerHTML = "";

        // Sample list of options
        var options = [
            "",
            "TERMINAL HANDLING CHARGES",
            "BL CHARGES",
            "VGM",
            "HALUAGE CHARGES",
            "AGENCY CHARGES",
            "BILL OF LADING",
            "CARTING CHARGES -(S)",
            "CERTIFICATE OF ORIGIN CHARGES",
            "CFS CHARGES",
            "COMMISSION",
            "COURIER CHARGES",
            "CUSTOM CLEARANCE CHARGES",
            "DOCUMENTATION CHARGES",
            "EDI REGISTRATION",
            "EXAMINATION CHARGES",
            "EX-WORK CHARGES",
            "FUMIGATION CHARGES",
            "HANDLING CHARGES -(S)",
            "IHC CHARGES",
            "INSURANCE",
            "LATE FEES",
            "LOADING CHARGES",
            "UNLOADING CHARGES",
            "LOCAL CHARGES",
            "MEASUREMENT CHARGES",
            "ORIGIN CHARGES",
            "PALLETIZATION CHARGES",
            "SEAL CHARGES",
            "TERMINAL HANDLING CHARGES",
            "TOLL FEE",
            "DELIVERY ORDER CHARGES",
            "DESTINATION DUTY",
            "TRANSPORTATION CHARGES"
            // Add more options as needed
        ];

        // Filter options based on input value
        options.forEach(function (option) {
            if (option.toUpperCase().includes(inputValue)) {
                var listItem = document.createElement("li");
                listItem.textContent = option;
                autocompleteList.appendChild(listItem);

                // Add click event listener to set input value on click
                listItem.addEventListener("click", function () {
                    input.value = option;
                    autocompleteList.style.display = "none"; // Hide the dropdown after selection
                });
            }
        });

        // Display the dropdown if there are matching options
        if (autocompleteList.childElementCount > 0) {
            autocompleteList.style.display = "block";
        } else {
            autocompleteList.style.display = "none";
        }
    });

    // Close dropdown when clicking outside the input or dropdown
    document.addEventListener("click", function (e) {
        if (!autocompleteContainer.contains(e.target)) {
            autocompleteList.style.display = "none";
        }
    });

    return autocompleteContainer;
}

function createSelectWithOptions() {
    // Create select element
    var select = document.createElement("select");

    // Set attributes for select
    select.setAttribute("name", "charges");

    // Add options to select
    var options = [
        "Pre Paid",
        "Collect"

        // Add more options as needed
    ];

    options.forEach(function (optionValue) {
        var option = document.createElement("option");
        option.text = optionValue;
        select.add(option);
    });

    return select;
}

/////////////////////////////////////////////////////////



// Freight calculations
document.addEventListener("DOMContentLoaded", function () {
    // Get the editable cells for freight calculations
    const quantityCell = document.getElementById("freight_quantity");
    const rateCell = document.getElementById("freight_rate");
    const amountCell = document.getElementById("freight_amount");
    const exchangeRateCell = document.getElementById("exchange_rate");
    const inINRCell = document.getElementById("in_INR");
    const gst5PercentCell = document.getElementById("GST5%");
    const totalCell = document.getElementById("freight_total");

    // Add event listeners for quantity and rate cells in freight
    quantityCell.addEventListener("input", updateFreightAmount);
    rateCell.addEventListener("input", updateFreightAmount);

    // Add event listener for exchange rate cell in freight
    exchangeRateCell.addEventListener("input", updateINRValue);

    // Function to update the freight amount
    function updateFreightAmount() {
        const quantity = parseFloat(quantityCell.textContent) || 0;
        const rate = parseFloat(rateCell.textContent) || 0;
        const freightAmount = quantity * rate;
        amountCell.innerHTML = `$${freightAmount.toFixed(2)}`;
        updateINRValue();
    }

    // Function to update the INR value, GST 5%, and total in freight
    function updateINRValue() {
        const freightAmount = parseFloat(amountCell.textContent.replace(/[^\d.]/g, '')) || 0; // Remove non-numeric characters
        const exchangeRate = parseFloat(exchangeRateCell.textContent) || 1;
        const inINRValue = freightAmount * exchangeRate;
        const gst5Percent = inINRValue * 0.05;
        const totalValue = inINRValue + gst5Percent;

        inINRCell.innerHTML = `₹${inINRValue.toFixed(2)}`;
        gst5PercentCell.innerHTML = `₹${gst5Percent.toFixed(2)}`;
        totalCell.innerHTML = `₹${totalValue.toFixed(2)}`;

        calculateOriginCharges(); // Added for updating origin charges
    }
});









// Origin calculations
var table = document.getElementById("origin_Table");

// Event listener for changes in quantity, rate, or amount cells in VGM row
table.addEventListener("input", function (event) {
    // Get the row number
    var rowNumber = event.target.parentNode.rowIndex;

    // Check if the description is "VGM"
    var descriptionInput = table.rows[rowNumber].cells[1].querySelector('input[type="text"]');
    if (descriptionInput.value.toLowerCase() === "vgm") {
        // Calculate the amount for the "VGM" row with quantity * rate * exchange rate
        calculateVGMAmount(rowNumber);
    } else {
        // Calculate the amount for the corresponding row
        calculateAmount(rowNumber);
    }

    // Calculate the total amount for the origin table
    calculateTotalAmount();
});

// Event listener for changes in the exchange rate
var exchangeRateCell = document.getElementById("exchange_rate");
exchangeRateCell.addEventListener("input", function () {
    // Calculate the amount for the "VGM" row when the exchange rate changes
    calculateVGMAmount(3);
});

// Function to calculate amount for other rows in origin
function calculateAmount(rowNumber) {
    var quantity = parseFloat(table.rows[rowNumber].cells[3].innerHTML) || 0;
    var rate = parseFloat(table.rows[rowNumber].cells[4].innerHTML) || 0;
    var amount = quantity * rate;
    table.rows[rowNumber].cells[5].innerHTML = `₹${amount.toFixed(2)}`;

    var totalAmount = 0;

    // Iterate over all rows above the origin_total row
    for (var i = 1; i < table.rows.length - 3; i++) {
        var amount = parseFloat(table.rows[i].cells[5].innerHTML.replace(/[^\d.]/g, '')) || 0; // Remove non-numeric characters
        totalAmount += amount;
    }

    document.getElementById("origin_total").innerHTML = `₹${totalAmount.toFixed(2)}`;

    // 18% GST
    var gst18Percent = totalAmount * 0.18;
    document.getElementById("18%GST").innerHTML = `₹${gst18Percent.toFixed(2)}`;

    calculateGrandTotal(); // Added for updating grand total
}

// Function to calculate amount for VGM row in origin
function calculateVGMAmount(rowNumber) {
    // Get the quantity, rate, and exchange rate values from the input fields
    var quantity = parseFloat(table.rows[rowNumber].cells[3].innerHTML) || 0;
    var rate = parseFloat(table.rows[rowNumber].cells[4].innerHTML) || 0;
    var exchangeRate = parseFloat(exchangeRateCell.innerHTML) || 1;

    // Calculate the amount with exchange rate and update the amount cell
    var amount = quantity * rate * exchangeRate;
    table.rows[rowNumber].cells[5].innerHTML = `₹${amount.toFixed(2)}`;

    var totalAmount = 0;

    // Iterate over all rows above the origin_total row
    for (var i = 1; i < table.rows.length - 3; i++) {
        var amount = parseFloat(table.rows[i].cells[5].innerHTML.replace(/[^\d.]/g, '')) || 0; // Remove non-numeric characters
        totalAmount += amount;
    }

    document.getElementById("origin_total").innerHTML = `₹${totalAmount.toFixed(2)}`;

    // 18% GST
    var gst18Percent = totalAmount * 0.18;
    document.getElementById("18%GST").innerHTML = `₹${gst18Percent.toFixed(2)}`;

    calculateGrandTotal(); // Added for updating grand total
}

// Function to calculate grand total
function calculateGrandTotal() {
    var totalAmount = parseFloat(document.getElementById("origin_total").innerHTML.replace(/[^\d.]/g, '')) || 0; // Remove non-numeric characters
    var gst18Percent = totalAmount * 0.18;

    // Grand total
    var grandTotal = totalAmount + gst18Percent;
    document.getElementById("Origin_Grand_Total").innerHTML = `₹${grandTotal.toFixed(2)}`;
}












// Destination calculations
var destinationTable = document.getElementById("destination_table");

// Event listener for changes in quantity, rate, or amount cells in destination table
destinationTable.addEventListener("input", function (event) {
    // Get the row number
    var rowNumber = event.target.parentNode.rowIndex;

    // Check if it's not the last row (total amount row)
    if (rowNumber < destinationTable.rows.length - 1) {
        // Calculate the amount for the corresponding row
        calculateDestinationAmount(rowNumber);

        // Calculate the total amount for the destination table
        calculateDestinationTotalAmount();
    }
});

// Function to calculate amount for a row in destination table
// Function to calculate amount for a row in destination table
function calculateDestinationAmount(rowNumber) {
    var quantity = parseFloat(destinationTable.rows[rowNumber].cells[3].innerText) || 0;
    var rate = parseFloat(destinationTable.rows[rowNumber].cells[4].innerText) || 0;
    var amount = quantity * rate;
    destinationTable.rows[rowNumber].cells[5].innerText = `₹${amount.toFixed(2)}`;
}

// Function to calculate total amount for destination table
function calculateDestinationTotalAmount() {
    var totalAmount = 0;

    // Iterate over all rows above the destination_total row
    for (var i = 1; i < destinationTable.rows.length - 1; i++) {
        var amount = parseFloat(destinationTable.rows[i].cells[5].innerText.replace(/[^\d.]/g, '')) || 0; // Remove non-numeric characters
        totalAmount += amount;
    }

    document.getElementById("destination_total").innerText = `₹${totalAmount.toFixed(2)}`;
}


