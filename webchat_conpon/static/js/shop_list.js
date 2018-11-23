// $(document).ready(function () {
//     var paras = document.getElementsByTagName("meta");
//     var content = paras[0].getAttribute("content");
//     var host = window.location.host;
//     var url = 'http://' + host + '/shopapi?keyword_id=' + content +'&page=1';
//     $.ajax({
//         type: "get",
//         url: url,
//         dataType: "json",
//         data: "",
//         success: function (shop) {
//             for (var i=0;i<shop.length;i++) {
//                 $("#master_map_url").append('<img src='+ shop[i].shop_master_map_url +' class="list-pic" />');
//                 $("#commodity_name").append('<a href="detail.html">shop[i].commodity_name}</a>');
//                 $("#shop_price").append(shop[i].shop_price);
//                 $("#shop_volume").append(shop[i].shop_volume);
//                 $("#coupon_denomination_value").append(shop[i].coupon_denomination_value);
//             }
//             // var tbody = $('<tbody></tbody>');
//             // for (var i = 0; i < data.length; i++) {
//             //     var tr = $('<tr></tr>');
//             //     tr.append('<td>' + data[i].filename + '</td>' + '<td>' + data[i].filesize + '</td>' + '<td>' + data[i].fileauthority + '</td>' + '<td>' + data[i].filedate + ' </td>');
//             //     tbody.append(tr);
//
//             }
//             // $('#myTable tbody').replaceWith(tbody);
//
//     });
// });

function fn1(){
    return 100;
}

function GetQueryString(name)
{
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);//search,查询？后面的参数，并匹配正则
     if(r!=null)return  unescape(r[2]); return null;
}

function GetPageCount(){
    var classify = GetQueryString("keyword_id");
    var host = window.location.host;
    var pagecounturl = 'http://' + host + '/pagecount?classify=' + classify;

    $.ajax({
        type: "GET",
        url: pagecounturl,
        datatype: "json",
        async:false,
        data: "",
        success: function (count) {
            pagecount = count;
            // alert(pagecount)

        },
        error:function(){
            pagecount = 1
        }

    });
     return pagecount;
}



window.onload=function() {
    //--------------上拉加载更多---------------
    //获取滚动条当前的位置
    function getScrollTop() {
        var scrollTop = 0;
        if (document.documentElement && document.documentElement.scrollTop) {
            scrollTop = document.documentElement.scrollTop;
        } else if (document.body) {
            scrollTop = document.body.scrollTop;
        }
        return scrollTop;
    }


    //获取当前可视范围的高度
    function getClientHeight() {
        var clientHeight = 0;
        if (document.body.clientHeight && document.documentElement.clientHeight) {
            clientHeight = Math.min(document.body.clientHeight, document.documentElement.clientHeight);
        } else {
            clientHeight = Math.max(document.body.clientHeight, document.documentElement.clientHeight);
        }
        return clientHeight;
    }

    //获取文档完整的高度
    function getScrollHeight() {
        return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
    }

    // alert(getScrollTop());
    // alert(getClientHeight());
    // alert(getScrollHeight());
    //滚动事件触发
    window.onscroll = function () {
        if (parseInt(getScrollTop() + 1) + getClientHeight() >= getScrollHeight()) {
            $("#jiazai").text('加载中……');
            page = GetPageCount() - 1;
            // console.log(urlhost);
            // alert(requestapi());
            // requestapi();
            test(page);
            page--;

            }


            // alert(urlhost);
            // requestapi();
            // document.getElementById("link").click();
        }



};


function test(page) {
    var keyword_id = GetQueryString("keyword_id");
    var host = window.location.host;
    urlhost = 'http://' + host + '/shopapi?keyword_id='+ keyword_id +'&page=' + page;
    // alert(urlhost);
    $.ajax({
        type: "GET",
        url: urlhost,
        datatype: "json",
        async: false,
        data: "",
        success: function (shop) {
            // alert(shop.length);
            // data = JSON.parse(shop);
            // alert(shop.length);
            for (var i=0;i<shop.length; i++){
                $("#incomeNum").append('<li><a href="detail.html"><img   src="' +  shop[i].shop_master_map_url + '"class="list-pic" /></a><div class="shop-list-mid"><div class="text_chang"><a href="detail.html">'+ shop[i].commodity_name +'</a></div><div class=""></div><table><tr><td class="text_yangshi" style="text-decoration: line-through;">原价 ￥'+ shop[i].shop_price +'</td><td class="text_yangshi" style="width: 50%;text-align: right">销量 ' + shop[i].shop_volume + '</td></tr><tr><td class="text_yangshi">券后价￥10</td></tr></table><div><div style="width: 55px;height: 18px;background:rgb(246, 90, 16);line-height:18px;color: #fff;display: inline-block;text-align: center"><span style="margin-left: -6px;font-size: 10px">券' + shop[i].coupon_denomination_value +'元</span></div>\n' +
                    '<span style="border-right:1px dashed #fff;position: relative;left: -14px;"></span>\n' +
                    '<div style="width: 10px;height: 10px;border-radius: 50%;background: #fff;display: inline-block;margin-left: -10px;position: relative;"></div></div></div>\n' +
                    '<div class="list-cart"><div style="width: 50px;height: 50px"><img src="../static/images/test.png" height="70" width="55"/></a></div></div></li>');
            }
            // alert(shop[0].commodity_name);
            // $("#incomeNum").append('<p>interval:'+shop.commodity_name+'</p>');
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            // alert(XMLHttpRequest.status);
            // alert(XMLHttpRequest.readyState);
            // alert(textStatus);
        },
        complete: function (XMLHttpRequest, textStatus) {
            this; // 调用本次AJAX请求时传递的options参数
        }
    })

}


function requestapi() {
    $.ajax({
        type: "GET",
        url: urlhost,
        datatype: "json",
        data: "",
        success: function (data) {
            if (data.list.length = 20) {
                htmltxt += '<div class=\"text_chang\"><a href=\"detail.html\">' + data.commodity_name + '</a></div>'
                $("#incomeNum").append(htmltxt);
            }
            else {
                htmltxt += '<div class=\"text_chang\"><a href=\"#\">' + "not " + '</a></div>'

            }
        },
        error: function () {
            htmltxt += '<div class=\"text_chang\"><a href=\"#\">' + "error " + '</a></div>'

        }


    });
}

        //-----------------结束--------------------