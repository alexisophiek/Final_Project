


console.log('nrc_lexicon.js loaded')

function nrc(){

	d3.json('/NRC_lexicon', function(data){
		console.log(data)
		return data
	})
}

nrc()