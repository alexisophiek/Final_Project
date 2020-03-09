
function tableBuilder(inputData) {
    var tbody = d3.select('.table');
    tbody.html("");
    head = tbody.append("thead")
    headerRow = head.append("tr")
    header = headerRow.append("th")
    header.text("Sentiments")
    header = headerRow.append("th")
    header.text("Tokenized Tweets")
    inputData.forEach(tweets => {
        var row = tbody.append('tr').attr('class','table-row');
        Object.entries(tweets).forEach(([key,value]) => {
            var cell = row.append('td');
            cell.text(value);
        })
    })
}
d3.json("/cleaned_tweets", function(data) {
   tableBuilder(data);
});