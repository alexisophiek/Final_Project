
console.log('data is loading')

function nrc(){

	d3.json('/tweets', function(data){
		console.log(data)
		return data
	})
}

nrc()