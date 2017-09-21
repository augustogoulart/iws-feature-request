function FeatureRequestViewModel() {
    var self = this;

    self.requests = ko.observable();
    self.requestDetail = ko.observable();

    self.getRequests = function(){
        self.requestDetail(null);
        $.get('/api/requests/', self.requests );
    };

    self.getRequestDetail = function (request) {
        self.requests(null);
        $.get('/api/requests/'+request.id, self.requestDetail)
    };

    self.deleteRequest = function (message) {
        $.ajax({
            url:'/api/requests/'+message.id,
            type: 'DELETE',
            data: {message:message},
            success: function() {
                self.getRequests();
             }
        })

    };

    self.getRequests();
}

ko.applyBindings(new FeatureRequestViewModel());