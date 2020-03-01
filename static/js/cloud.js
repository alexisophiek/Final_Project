
function drawWordCloud(word_count){
    console.log("start function")
    var svg_location = "#chart";
    var width = '500px';
    var height = '500px';

    // var fill = d3.scale.category20();

    // Object.entries(word_count).forEach(([key,value]) => console.log(`Word: ${key} - Count: ${value}`))

    // console.log(typeof(word_count))
    // var word_entries = Object.entries(word_count)/
    var word_entries = []
    var words = []
    console.log("Got entries")
    var words = [] 
    Object.entries(word_count).forEach(([key,value]) => {
        words.push(key);
        word_entries.push(value)
    });
    // console.log(`Entries ${word_entries}`)

    var xScale = d3.scaleLinear()
    .domain([0, d3.max(word_entries)
    ])
    .range([10,100]);

    console.log("got xScale")

    d3.layout.cloud().size([width, height])
    .timeInterval(20)
    .words(words)
    .fontSize(word_entries.forEach(d=> { return xScale(+d); }))
    .text(words.forEach(d=> { return d; }))
    .rotate(function() { return ~~(Math.random() * 2) * 90; })
    .font("Impact")
    .on("end", draw)
    .start();

    console.log("layout start")

    function draw(words) {
        console.log("drawing")
    d3.select(svg_location).append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + [width >> 1, height >> 1] + ")")
        .selectAll("text")
        .data(words)
        .enter().append("text")
        .style("font-size", word_entries.forEach(d=> { return xScale(+d) +"px"; }))
        .style("font-family", "Impact")
        // .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.key; });
    }


    // d3.layout.cloud().stop();
}


d3.json("../static/js/words.json", function(words) {
    console.log(words);
    drawWordCloud(words);
})
    