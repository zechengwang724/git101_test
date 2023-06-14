function double(x){
	return x*2
}

function triple(x){
	return x*3
}

module.exports = {
	double: double,
	triple: triple,
}

exports.double = double
exports.triple = triple
