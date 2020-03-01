var data 
console.log('get_tweets.js loaded')

function yourTweets(){

	d3.json('/get_tweets', function(data){
		console.log('data ',data)
		// console.log(data.type())
		return data
// 	})
// 	return data
// }

	console.log(data.length())
	return data
})
	// return data
}

yourTweets()

console.log()

var map = d3.select('#map')

// map.addTo()

// alert(length(data))

// data.forEach(function(d, i){
// 	data.

// console.log(data)

// d3.select('#vis')