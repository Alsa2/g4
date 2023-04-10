function PostpopulateSecondDropdown() {
  var firstDropdown = document.getElementById("Post_first-dropdown");
  var secondDropdown = document.getElementById("Post_second-dropdown");

  // Clear the options in the second dropdown
  secondDropdown.innerHTML = "";

  // Get the selected value from the first dropdown
  var selectedValue = firstDropdown.value;

  // Create options for the second dropdown based on the selected value
  if (selectedValue === "top") {
    var all = document.createElement("option");
    all.value = "all";
    all.text = "All Time";
    secondDropdown.add(all);

    var hour = document.createElement("option");
    hour.value = "hour";
    hour.text = "Last Hour";
    secondDropdown.add(hour);

    var day = document.createElement("option");
    day.value = "day";
    day.text = "Last Day";
    secondDropdown.add(day);

    var week = document.createElement("option");
    week.value = "week";
    week.text = "Last Week";
    secondDropdown.add(week);

    var month = document.createElement("option");
    month.value = "month";
    month.text = "Last Month";
    secondDropdown.add(month);

    var year = document.createElement("option");
    year.value = "year";
    year.text = "Last Year";
    secondDropdown.add(year);
  }

  // Hide/show the second dropdown based on the selected value
  if (selectedValue === "new") {
    window.location.href = "/?post_category=new";
    secondDropdown.style.display = "none";
  } else if (selectedValue === "random") {
    window.location.href = "/?post_category=random";
    secondDropdown.style.display = "none";
  } else {
    secondDropdown.style.display = "block";
  }
}
  
  // Redirect to the appropriate URL when an option is selected from the second dropdown
function PostredirectforsecondDropdown() {
  var secondDropdown = document.getElementById("Post_second-dropdown");
  var timeValue = secondDropdown.value;
  window.location.href = "/?post_category=top&post_time=" + timeValue;
}

function PostsetDropdownValuesFromUrlParams() {
  console.log("PostsetDropdownValuesFromUrlParams");
  const urlParams = new URLSearchParams(window.location.search);
  const post_category = urlParams.get('post_category');
  const post_time = urlParams.get('post_time');

  const firstDropdown = document.getElementById('Post_first-dropdown');
  const secondDropdown = document.getElementById('Post_second-dropdown');

  // Set the selected value of the first dropdown
  if (post_category === 'top') {
    firstDropdown.value = 'top';
  } else if (post_category === 'new') {
    firstDropdown.value = 'new';
    secondDropdown.style.display = "none";
  } else if (post_category === 'random') {
    firstDropdown.value = 'random';
    secondDropdown.style.display = "none";
  } else {
    firstDropdown.value = 'top';
    secondDropdown.value = 'all';
  }

  // Set the selected value of the second dropdown
  if (post_time === 'all') {
    secondDropdown.value = 'all';
  } else if (post_time === 'hour') {
    secondDropdown.value = 'hour';
  } else if (post_time === 'day') {
    secondDropdown.value = 'day';
  } else if (post_time === 'week') {
    secondDropdown.value = 'week';
  } else if (post_time === 'month') {
    secondDropdown.value = 'month';
  } else if (post_time === 'year') {
    secondDropdown.value = 'year';
  }
}




// TABLE FOR POSTS





function Table_populateSecondDropdown() {
  console.log("Table_populateSecondDropdown");
  var firstDropdown = document.getElementById("Table_first-dropdown");
  var secondDropdown = document.getElementById("Table_second-dropdown");

  // Clear the options in the second dropdown
  secondDropdown.innerHTML = "";

  // Get the selected value from the first dropdown
  var selectedValue = firstDropdown.value;

  // Create options for the second dropdown based on the selected value
  if (selectedValue === "top") {
    var all = document.createElement("option");
    all.value = "all";
    all.text = "All Time";
    secondDropdown.add(all);

    var hour = document.createElement("option");
    hour.value = "hour";
    hour.text = "Last Hour";
    secondDropdown.add(hour);

    var day = document.createElement("option");
    day.value = "day";
    day.text = "Last Day";
    secondDropdown.add(day);

    var week = document.createElement("option");
    week.value = "week";
    week.text = "Last Week";
    secondDropdown.add(week);

    var month = document.createElement("option");
    month.value = "month";
    month.text = "Last Month";
    secondDropdown.add(month);

    var year = document.createElement("option");
    year.value = "year";
    year.text = "Last Year";
    secondDropdown.add(year);
  }

  // Hide/show the second dropdown based on the selected value
  if (selectedValue === "new") {
    window.location.href = "/?table_category=new";
    secondDropdown.style.display = "none";
  } else if (selectedValue === "random") {
    window.location.href = "/?table_category=random";
    secondDropdown.style.display = "none";
  } else {
    secondDropdown.style.display = "block";
  }
}
  
  // Redirect to the appropriate URL when an option is selected from the second dropdown
function Table_redirectforsecondDropdown() {
  var secondDropdown = document.getElementById("Table_second-dropdown");
  var timeValue = secondDropdown.value;
  window.location.href = "/?table_category=top&table_time=" + timeValue;
}

function TablesetDropdownValuesFromUrlParams() {
  console.log("TablesetDropdownValuesFromUrlParams");
  const urlParams = new URLSearchParams(window.location.search);
  const post_category = urlParams.get('table_category');
  const post_time = urlParams.get('table_time');

  const firstDropdown = document.getElementById('Table_first-dropdown');
  const secondDropdown = document.getElementById('Table_second-dropdown');

  // Set the selected value of the first dropdown
  if (post_category === 'top') {
    firstDropdown.value = 'top';
  } else if (post_category === 'new') {
    firstDropdown.value = 'new';
    secondDropdown.style.display = "none";
  } else if (post_category === 'random') {
    firstDropdown.value = 'random';
    secondDropdown.style.display = "none";
  } else {
    firstDropdown.value = 'top';
    secondDropdown.value = 'all';
  }

  // Set the selected value of the second dropdown
  if (post_time === 'all') {
    secondDropdown.value = 'all';
  } else if (post_time === 'hour') {
    secondDropdown.value = 'hour';
  } else if (post_time === 'day') {
    secondDropdown.value = 'day';
  } else if (post_time === 'week') {
    secondDropdown.value = 'week';
  } else if (post_time === 'month') {
    secondDropdown.value = 'month';
  } else if (post_time === 'year') {
    secondDropdown.value = 'year';
  }
}



// TABLE FOR SEARCH





function Search_populateSecondDropdown() {
  const urlParams = new URLSearchParams(window.location.search);
  var currentSearch = urlParams.get('search');
  var firstDropdown = document.getElementById("Search_first-dropdown");
  var secondDropdown = document.getElementById("Search_second-dropdown");

  // Clear the options in the second dropdown
  secondDropdown.innerHTML = "";

  // Get the selected value from the first dropdown
  var selectedValue = firstDropdown.value;

  // Create options for the second dropdown based on the selected value
  if (selectedValue === "top") {
    var all = document.createElement("option");
    all.value = "all";
    all.text = "All Time";
    secondDropdown.add(all);

    var hour = document.createElement("option");
    hour.value = "hour";
    hour.text = "Last Hour";
    secondDropdown.add(hour);

    var day = document.createElement("option");
    day.value = "day";
    day.text = "Last Day";
    secondDropdown.add(day);

    var week = document.createElement("option");
    week.value = "week";
    week.text = "Last Week";
    secondDropdown.add(week);

    var month = document.createElement("option");
    month.value = "month";
    month.text = "Last Month";
    secondDropdown.add(month);

    var year = document.createElement("option");
    year.value = "year";
    year.text = "Last Year";
    secondDropdown.add(year);
  }

  // Hide/show the second dropdown based on the selected value
  if (selectedValue === "new") {
    window.location.href = "/search?search_category=new&search="+currentSearch;
    secondDropdown.style.display = "none";
  } else if (selectedValue === "random") {
    window.location.href = "/search?search_category=random&search="+currentSearch;
    secondDropdown.style.display = "none";
  } else {
    secondDropdown.style.display = "block";
  }
}
  
  // Redirect to the appropriate URL when an option is selected from the second dropdown
function Search_redirectforsecondDropdown() {
  const urlParams = new URLSearchParams(window.location.search);
  var currentSearch = urlParams.get('search');
  var secondDropdown = document.getElementById("Search_second-dropdown");
  var timeValue = secondDropdown.value;
  window.location.href = "/search?search_category=top&search_time=" + timeValue+"&search="+currentSearch;
}

function SearchsetDropdownValuesFromUrlParams() {
  console.log("SearchsetDropdownValuesFromUrlParams");
  const urlParams = new URLSearchParams(window.location.search);
  const post_category = urlParams.get('search_category');
  const post_time = urlParams.get('search_time');

  const firstDropdown = document.getElementById('Search_first-dropdown');
  const secondDropdown = document.getElementById('Search_second-dropdown');

  // Set the selected value of the first dropdown
  if (post_category === 'top') {
    firstDropdown.value = 'top';
  } else if (post_category === 'new') {
    firstDropdown.value = 'new';
    secondDropdown.style.display = "none";
  } else if (post_category === 'random') {
    firstDropdown.value = 'random';
    secondDropdown.style.display = "none";
  } else {
    firstDropdown.value = 'top';
    secondDropdown.value = 'all';
  }

  // Set the selected value of the second dropdown
  if (post_time === 'all') {
    secondDropdown.value = 'all';
  } else if (post_time === 'hour') {
    secondDropdown.value = 'hour';
  } else if (post_time === 'day') {
    secondDropdown.value = 'day';
  } else if (post_time === 'week') {
    secondDropdown.value = 'week';
  } else if (post_time === 'month') {
    secondDropdown.value = 'month';
  } else if (post_time === 'year') {
    secondDropdown.value = 'year';
  }
}
