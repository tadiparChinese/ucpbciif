define(function () {
    'use strict';

    var app = angular.module('app');

    app.controller('AmortizationListController', function AmortizationListController(
        $http,
        $filter,
        $scope,
        $state,
        $timeout,
        toastr,
        appFactory,
        NgTableParams,
        $window
    ) {
        $scope.tableAmortization = new NgTableParams(
            {
                page: 1,
                count: 10,
            },
            {
                counts: [10, 20, 30, 50, 100],
                getData: function (params) {
                    return $http.get('/api/loans/amortizationitems/', { params: $scope.params }).then(
                        function (response) {
                            console.log(response.data);
                            var filteredData = params.filter()
                                ? $filter('filter')(response.data, params.filter())
                                : response.data;
                            var orderedData = params.sorting()
                                ? $filter('orderBy')(filteredData, params.orderBy())
                                : filteredData;
                            var page = orderedData.slice(
                                (params.page() - 1) * params.count(),
                                params.page() * params.count()
                            );
                            params.total(response.data.length);

                            var page = orderedData.slice(
                                (params.page() - 1) * params.count(),
                                params.page() * params.count()
                            );
                            return page;
                        },
                        function (error) {
                            toastr.error(
                                'Error ' + error.status + ' ' + error.statusText,
                                'Could not load Amortization Lists. Please contact System Administrator.'
                            );
                        }
                    );
                },
            }
        );

        $scope.$watch(
            'searchTermAuto',
            function (newTerm, oldTerm) {
                $scope.tableAmortization.filter({ $: newTerm });
            },
            true
        );

        $scope.params = {};

        $scope.filters = [
            {
                name: 'Borrower',
                showFilter: false,
                filterFormat: 'uppercase',
                params: {
                    param1: 'borrowerId',
                },
            },
            {
                name: 'Term',
                showFilter: false,
                filterFormat: 'uppercase',
                params: {
                    param1: 'term',
                },
            },
            {
                name: 'Amortization Amount Range',
                showFilter: false,
                filterFormat: "currency :'₱'",
                params: {
                    param1: 'creditLineAmountFrom',
                    param2: 'creditLineAmountTo',
                },
            },
            {
                name: 'Total Availment Range',
                showFilter: false,
                filterFormat: "currency :'₱'",
                params: {
                    param1: 'totalAvailmentFrom',
                    param2: 'totalAvailmentTo',
                },
            },
            {
                name: 'Interest Range',
                showFilter: false,
                filterFormat: 'staticPercentage',
                params: {
                    param1: 'interestFrom',
                    param2: 'interestTo',
                },
            },
            {
                name: 'Date Approved Range',
                showFilter: false,
                filterFormat: "date : 'mediumDate'",
                params: {
                    param1: 'dateApprovedFrom',
                    param2: 'dateApprovedTo',
                },
            },
            {
                name: 'Expiry Date Range',
                showFilter: false,
                filterFormat: "date : 'mediumDate'",
                params: {
                    param1: 'expiryDateFrom',
                    param2: 'expiryDateTo',
                },
            },
        ];

        $scope.showFilterButton = false;

        $scope.showFilter = function (filter) {
            if (filter.showFilter) {
                filter.showFilter = false;
            } else {
                filter.showFilter = true;
            }

            for (var i = 0; i < $scope.filters.length; i++) {
                if ($scope.filters[i].showFilter == true) {
                    $scope.showFilterButton = true;
                    break;
                } else {
                    $scope.showFilterButton = false;
                }
            }
        };

        $scope.applyFilter = function () {
            angular.forEach($scope.filters, function (filter) {
                if (!filter.showFilter) {
                    angular.forEach(filter.params, function (value, key) {
                        delete $scope.params[value];
                    });
                }
            });
            $scope.tableAmortization.reload();
        };

        $scope.resetFilter = function () {
            angular.forEach($scope.filters, function (filter) {
                filter.showFilter = false;
            });
            $scope.showFilterButton = false;
            $scope.params = {};
            $scope.tableAmortization.reload();
        };

        $scope.view = function (loanId) {
             
            $state.go('app.loans.info', { loanId: loanId });
        };

        $scope.retrieveHeaders = function () {
            var headers = [];
            var ngTable = document.getElementById('tableAmortization');
            var rowLength = ngTable.rows.length;

            for (var i = 0; i < rowLength; i++) {
                var ngCells = ngTable.rows.item(i).cells;
                var cellLength = ngCells.length;

                for (var j = 0; j < cellLength; j++) {
                    var cellTitle = ngCells.item(j).getAttribute('data-title');
                    if (cellTitle && cellTitle != "'ACTIONS'") {
                        cellTitle = cellTitle.slice(1, -1);
                        if (!headers.includes(cellTitle)) {
                            headers.push(cellTitle);
                        }
                    }
                }
            }
            return headers;
        };

        $scope.retrieveCellValues = function () {
            var values = [];
            var ngTable = document.getElementById('tableAmortization');
            var rowLength = ngTable.rows.length;

            for (var i = 2; i < rowLength; i++) {
                var exclude = ngTable.rows.item(i).getAttribute('print-exclude');
                if (!exclude) {
                    var ngCells = ngTable.rows.item(i).cells;
                    var cellLength = ngCells.length;
                    var cells = [];
                    for (var j = 0; j < cellLength; j++) {
                        if (ngCells.item(j).innerText) {
                            cells.push(ngCells.item(j).innerText);
                        }
                    }
                    values.push(cells);
                }
            }
            return values;
        };

        $scope.loadCurrentUserInfo = function () {
            var user = {};
            appFactory.getCurrentUserInfo().then(function (data) {
                user['name'] = data.fullName;
                user['position'] = data.committeePosition;
            });
            return user;
        };

        $scope.printDataTable = function () {
            var filters = [];
            angular.forEach($scope.filters, function (filter) {
                if (filter.showFilter) {
                    var parameters = {};
                    angular.forEach(filter.params, function (param) {
                        parameters[param] = $scope.params[param];
                    });
                    filters.push({
                        name: filter.name,
                        filterFormat: filter.filterFormat,
                        params: parameters,
                    });
                }
            });
            if ($scope.searchTermAuto) {
                filters.push({
                    name: 'Search',
                    filterFormat: 'uppercase',
                    params: { input: $scope.searchTermAuto },
                });
            }
            var $popup = $window.open('/print/amortizations', '_blank', 'directories=0,width=800,height=800');
            $popup.title = 'Amortization List';
            $popup.user = $scope.loadCurrentUserInfo();
            $popup.filters = filters;
            $popup.headers = $scope.retrieveHeaders();
            $popup.cellValues = $scope.retrieveCellValues();
        };
    });



    app.controller('MaturingAmortizationListController', function MaturingAmortizationListController(
        $http,
        $filter,
        $scope,
        $state,
        $timeout,
        toastr,
        appFactory,
        NgTableParams,
        $window
    ) {
        $scope.tableMaturingAmortization = new NgTableParams(
            {
                page: 1,
                count: 10,
            },
            {
                counts: [10, 20, 30, 50, 100],
                getData: function (params) {
                    return $http.get('/api/loans/amortizationitems/',  { params: { maturing: 'TRUE' } }).then(
                        function (response) {
                            console.log(response.data);
                            var filteredData = params.filter()
                                ? $filter('filter')(response.data, params.filter())
                                : response.data;
                            var orderedData = params.sorting()
                                ? $filter('orderBy')(filteredData, params.orderBy())
                                : filteredData;
                            var page = orderedData.slice(
                                (params.page() - 1) * params.count(),
                                params.page() * params.count()
                            );
                            params.total(response.data.length);

                            var page = orderedData.slice(
                                (params.page() - 1) * params.count(),
                                params.page() * params.count()
                            );
                            return page;
                        },
                        function (error) {
                            toastr.error(
                                'Error ' + error.status + ' ' + error.statusText,
                                'Could not load Maturing Amortization Lists. Please contact System Administrator.'
                            );
                        }
                    );
                },
            }
        );

        $scope.$watch(
            'searchTermAuto',
            function (newTerm, oldTerm) {
                $scope.tableMaturingAmortization.filter({ $: newTerm });
            },
            true
        );

        $scope.params = {};

        $scope.filters = [
            {
                name: 'Borrower',
                showFilter: false,
                filterFormat: 'uppercase',
                params: {
                    param1: 'borrowerId',
                },
            },
            {
                name: 'Term',
                showFilter: false,
                filterFormat: 'uppercase',
                params: {
                    param1: 'term',
                },
            },
            {
                name: 'Amortization Amount Range',
                showFilter: false,
                filterFormat: "currency :'₱'",
                params: {
                    param1: 'creditLineAmountFrom',
                    param2: 'creditLineAmountTo',
                },
            },
            {
                name: 'Total Availment Range',
                showFilter: false,
                filterFormat: "currency :'₱'",
                params: {
                    param1: 'totalAvailmentFrom',
                    param2: 'totalAvailmentTo',
                },
            },
            {
                name: 'Interest Range',
                showFilter: false,
                filterFormat: 'staticPercentage',
                params: {
                    param1: 'interestFrom',
                    param2: 'interestTo',
                },
            },
            {
                name: 'Date Approved Range',
                showFilter: false,
                filterFormat: "date : 'mediumDate'",
                params: {
                    param1: 'dateApprovedFrom',
                    param2: 'dateApprovedTo',
                },
            },
            {
                name: 'Expiry Date Range',
                showFilter: false,
                filterFormat: "date : 'mediumDate'",
                params: {
                    param1: 'expiryDateFrom',
                    param2: 'expiryDateTo',
                },
            },
        ];

        $scope.showFilterButton = false;

        $scope.showFilter = function (filter) {
            if (filter.showFilter) {
                filter.showFilter = false;
            } else {
                filter.showFilter = true;
            }

            for (var i = 0; i < $scope.filters.length; i++) {
                if ($scope.filters[i].showFilter == true) {
                    $scope.showFilterButton = true;
                    break;
                } else {
                    $scope.showFilterButton = false;
                }
            }
        };

        $scope.applyFilter = function () {
            angular.forEach($scope.filters, function (filter) {
                if (!filter.showFilter) {
                    angular.forEach(filter.params, function (value, key) {
                        delete $scope.params[value];
                    });
                }
            });
            $scope.tableMaturingAmortization.reload();
        };

        $scope.resetFilter = function () {
            angular.forEach($scope.filters, function (filter) {
                filter.showFilter = false;
            });
            $scope.showFilterButton = false;
            $scope.params = {};
            $scope.tableMaturingAmortization.reload();
        };

        $scope.view = function (loanId) {
             
            $state.go('app.payments.new', { loanId: loanId });
        };

        $scope.retrieveHeaders = function () {
            var headers = [];
            var ngTable = document.getElementById('tableMaturingAmortization');
            var rowLength = ngTable.rows.length;

            for (var i = 0; i < rowLength; i++) {
                var ngCells = ngTable.rows.item(i).cells;
                var cellLength = ngCells.length;

                for (var j = 0; j < cellLength; j++) {
                    var cellTitle = ngCells.item(j).getAttribute('data-title');
                    if (cellTitle && cellTitle != "'ACTIONS'") {
                        cellTitle = cellTitle.slice(1, -1);
                        if (!headers.includes(cellTitle)) {
                            headers.push(cellTitle);
                        }
                    }
                }
            }
            return headers;
        };

        $scope.retrieveCellValues = function () {
            var values = [];
            var ngTable = document.getElementById('tableMaturingAmortization');
            var rowLength = ngTable.rows.length;

            for (var i = 2; i < rowLength; i++) {
                var exclude = ngTable.rows.item(i).getAttribute('print-exclude');
                if (!exclude) {
                    var ngCells = ngTable.rows.item(i).cells;
                    var cellLength = ngCells.length;
                    var cells = [];
                    for (var j = 0; j < cellLength; j++) {
                        if (ngCells.item(j).innerText) {
                            cells.push(ngCells.item(j).innerText);
                        }
                    }
                    values.push(cells);
                }
            }
            return values;
        };

        $scope.loadCurrentUserInfo = function () {
            var user = {};
            appFactory.getCurrentUserInfo().then(function (data) {
                user['name'] = data.fullName;
                user['position'] = data.committeePosition;
            });
            return user;
        };

        $scope.printDataTable = function () {
            var filters = [];
            angular.forEach($scope.filters, function (filter) {
                if (filter.showFilter) {
                    var parameters = {};
                    angular.forEach(filter.params, function (param) {
                        parameters[param] = $scope.params[param];
                    });
                    filters.push({
                        name: filter.name,
                        filterFormat: filter.filterFormat,
                        params: parameters,
                    });
                }
            });
            if ($scope.searchTermAuto) {
                filters.push({
                    name: 'Search',
                    filterFormat: 'uppercase',
                    params: { input: $scope.searchTermAuto },
                });
            }
            var $popup = $window.open('/print/maturingamortizations', '_blank', 'directories=0,width=800,height=800');
            $popup.title = 'Maturing Amortization List';
            $popup.user = $scope.loadCurrentUserInfo();
            $popup.filters = filters;
            $popup.headers = $scope.retrieveHeaders();
            $popup.cellValues = $scope.retrieveCellValues();
        };
    });
});