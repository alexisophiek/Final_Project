
console.log('get_tweets.js loaded')

function yourTweets(data) {
	d3.xml('/cleaned_tweets', function (data) {
		// console.log(data)
		return data
	})
};



// The table generation function
function tabulate(data, columns) {
    var table = d3.select(".classified-tweets").append("table")
            .attr("style", "margin-left: 250px"),
        thead = table.append("thead"),
        tbody = table.append("tbody");

    // append the header row
    thead.append("tr")
        .selectAll("th")
        .data(columns)
        .enter()
        .append("th")

    // create a row for each object in the data
    var rows = tbody.selectAll("tr")
        .data(data)
        .enter()
        .append("tr");

    // create a cell in each row for each column
    var cells = rows.selectAll("td")
        .data(function(row) {
            return columns.map(function(column) {
                return {column: column, value: row[column]};
            });
        })
        .enter()
        .append("td")
        .attr("style", "font-family: Courier") // sets the font style
            .html(function(d) { return d.value; });
    
    return table;
}

// render the table
 var tweet_testtable = tabulate(yourTweets(), ["Tweet Tokens", "Sentiment"]);
 