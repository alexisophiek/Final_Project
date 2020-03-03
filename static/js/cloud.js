
function generateWordCloud(data) {
    anychart.onDocumentReady(function() {
        // code to create a word cloud chart will be here
        var chart = anychart.tagCloud(data)

        // set a chart title
    chart.title('Political Words and Sentiment')
    // set an array of angles at which the words will be laid out
    chart.angles([0])
    // enable a color range
    chart.colorRange(true)
    // set the color range length
    chart.colorRange().length('80%')
    chart.background().fill("transparent");
    
    // display the word cloud chart
    chart.container("container")
    chart.draw()
    })
};

d3.json("/word_cloud", function(data) {
    // var wordArray = Object.keys(data).map(i => data[i]);
    console.log(data)
    generateWordCloud(data)
});
