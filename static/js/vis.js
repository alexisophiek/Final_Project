console.log('~ ~  ~ ~ ~ vis.js connected ~  ~ ~ ')
	var dates = []
	var dateStrings = []

var data 
console.log('get_tweets.js loaded')

function yourTweets(){
	console.log('running tweets func . . . ')

	d3.json('/tweets', function(data){

		expected = data['data'][1]
		console.log(typeof(expected))
		console.log(typeof(expected['data']))
		console.log(expected)

		unexpected = data['data'][2503]
		console.log(typeof(unexpected))
		console.log(typeof(unexpected['data']))
		console.log(unexpected)
		// console.log(data.type())
		// return data

	for (i = 0; i < data.length; i++) {
		var time = data[i]['data']['timestamp_ms']
		time = parseInt(time * 1000)
		var dateObj = new Date(time * 1000)

var hours = dateObj.getUTCHours();
// Get minutes part from the timestamp 
var minutes = dateObj.getUTCMinutes(); 
// Get seconds part from the timestamp 
var seconds = dateObj.getUTCSeconds();
var formattedTime = hours.toString().padStart(2, '0') + ':' +  
                minutes.toString().padStart(2, '0') + ':' +  
                seconds.toString().padStart(2, '0'); 
		// // time = time.date
		dates.push(formattedTime)
		// dateStrings.push(dateString)
	}
	console.log(dates)
	// console.log(dateStrings)
	return data
	})
	// return data
}

yourTweets()
console.log(dates)

var vis = d3.select('#vis')


var trace1 = {
  x: [],
  y: [],
  mode: 'markers',
  type: 'scatter'
};

Plotly.newPlot('vis', data);
