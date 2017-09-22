function FeatureRequestViewModel() {
    var self = this;

    self.title = ko.observable();
    self.description = ko.observable();
    self.client = ko.observable();
    self.target_date = ko.observable();
    self.priority = ko.observable();
    self.product_area = ko.observable();


    self.requests = ko.observable();
    self.requestDetail = ko.observable();

    self.submitSuccess = ko.observable();
    self.formInvalid = ko.observable();

    self.setFalse = function () {
        self.submitSuccess(false);
    };

    self.getRequests = function () {
        self.requestDetail(null);
        $.get('/api/requests/', self.requests);
    };

    self.getRequestDetail = function (request) {
        self.requests(null);
        $.get('/api/requests/' + request.id, self.requestDetail)
    };

    self.deleteRequest = function (message) {
        $.ajax({
            url: '/api/requests/' + message.id,
            type: 'DELETE',
            data: {message: message},
            success: function () {
                self.getRequests();
            }
        });

    };
    self.patchRequest = function (request) {
        console.log('VAL:'+request.title);
        $.ajax({
            url: '/api/requests/' + request.id,
            type: 'PATCH',
            contentType: "application/json",
            accepts: "application/json",
            dataType: 'json',
            data: JSON.stringify({
                title: request.title,
                client: request.client,
                description: request.description,
                target_date: request.target_date,
                priority: request.priority,
                product_area: request.product_area
            }),
            success: function (request) {
                $('#myModal').modal('hide');
                $('.modal-backdrop').remove();
                self.getRequestDetail(request)
            },

            error: function (jqXHR) {
                console.log("POST error: " + jqXHR.status);
            }
        });




    };
    self.getRequests();
    self.postRequest = function () {
        $.ajax({
            url: '/api/requests/',
            type: 'POST',
            contentType: "application/json",
            accepts: "application/json",
            dataType: 'json',
            data: JSON.stringify({
                title: self.title(),
                client: self.client(),
                description: self.description(),
                target_date: self.target_date(),
                priority: self.priority(),
                product_area: self.product_area()
            }),
            success: function () {
                self.submitSuccess(true);
                self.formInvalid(false);
                self.getRequests();
                self.title(null);
                self.client('Client');
                self.description(null);
                self.target_date(null);
                self.priority('Priority');
                self.product_area('Product area');
            },
            error: function (jqXHR) {
                console.log("POST error: " + jqXHR.status);
            }
        });

    };

    self.validate = function () {
        if(!self.title() || self.client() ==="Client" || !self.description()
            || !self.target_date() || self.priority() === "Priority" || self.priority() === 'Product area')
        {
            self.formInvalid(true);
        }else{
            self.postRequest();
        }
    };

    self.getRequests();
}

ko.applyBindings(new FeatureRequestViewModel());



























