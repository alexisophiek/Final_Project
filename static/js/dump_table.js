var data

function yourTweets(){

	d3.json('/tweets', function(data){
		console.log('data is... according to get_tweets....')
		console.log(data)
		// console.log('data ',data)
		// console.log('type is .... ', typeof(data))
		console.log('first data point in data issss.... . . . . . .','\n',data[0])
		console.log('length of data is . . . ', data.length)

var data = data[0,10]

		var titles = ['text','id']
		var table = d3.select('#table').append('table');
		// var titles = d3.keys(data[0,1]);
// var titles = d3.keys(data[0]);
		  var headers = table.append('thead').append('tr')
		                   .selectAll('th')
		                   .data(titles).enter()
		                   .append('th')
		                   .text(function (d) {
			                    return d;
		                    })
		                   // .on('click', function (d) {
		                	  //  headers.attr('class', 'header');
		                	   
		                	  //  if (sortAscending) {
		                	  //    rows.sort(function(a, b) { return b[d] < a[d]; });
		                	  //    sortAscending = false;
		                	  //    this.className = 'aes';
		                	  //  } else {
		                		 // rows.sort(function(a, b) { return b[d] > a[d]; });
		                		 // sortAscending = true;
		                		 // this.className = 'des';
		                	  //  }
		                	   
		                   // });
		  
		  var rows = table.append('tbody').selectAll('tr')
		               .data(data).enter()
		               .append('tr');
		  rows.selectAll('td')
		    .data(function (d) {
		    	return data['data'].map(function (k) {
		    		return { 'value': d[k], 'name': k};
		    	});
		    }).enter()
		    .append('td')
		    .attr('data-th', function (d) {
		    	return d.name;
		    })
		    .text(function (d) {
		    	return d.value;
		    });
	  });
}