console.log('~ ~  ~ ~ ~ vis.js connected ~  ~ ~ ')

// var vis = d3.select('#vis')


var data 
console.log('get_tweets.js loaded')

console.log((if data) 'if data')

function yourTweets(){
	console.log('running tweets func . . . ')

	d3.json('/tweets', function(data){
		console.log(data)
		// console.log(data.type())
		return data
// 	})
// 	return data
// }

	console.log(data.length())
	console.log(data)

	return data
	})
	// return data
}



yourTweets()
console.log(data)



var map = d3.select('#map')

// map.addTo()

// alert(length(data))

// data.forEach(function(d, i){
// 	data.

// console.log(data)

// d3.select('#vis')
// d3.json('emotions')

d3.json('/')




var trace1 = {
  x: [],
  y: [10, 15, 13, 17],
  mode: 'markers',
  type: 'scatter'
};

Plotly.newPlot('vis', data);
