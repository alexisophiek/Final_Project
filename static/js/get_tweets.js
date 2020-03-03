
function yourTweets(data) {
	d3.xml('/cleaned_tweets', function (data) {
		console.log(data)
		return data
	})
};


// from data.js
var tableData = data;
// YOUR CODE HERE!
var tbody = d3.select('tbody');
function tableBuilder(inputData) {
    tbody.html("");
    inputData.forEach(sightings => {
        var row = tbody.append('tr');
        Object.entries(sightings).forEach(([key,value]) => {
            var cell = row.append('td');
            cell.text(value);
        })
    })
}
tableBuilder(tableData);




// render the table
 