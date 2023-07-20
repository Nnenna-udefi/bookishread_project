$(document).ready(function () {
           $("#enter").on("input", function () {
               var input = $(this).val();
               if (input.length >= 2) {
                   $.ajax({
                       url: "/autocomplete",
                       type: "POST",
                       data: { book: input },
                       success: function (data) {
                           var datalist = $("#book_list");
                           datalist.empty();
                           data.forEach(function (item) {
                               datalist.append($("<option>").attr("value", item));
			   });
                       },
                   });
               }
           });
       });
