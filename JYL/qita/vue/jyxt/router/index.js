import Router from 'vue-router'
import mainpage from '@/components/mainpage'
import stock from '@/components/stock'
import stockspec from '@/components/stockspec'
import indicator from '@/components/indicator'
import indicatorspec from '@/components/indicatorspec'
import stockhs300spec from '@/components/stockhs300spec'
import empty from '@/components/empty'
import information from '@/components/information'
import testpage from '@/components/testInsert/testPAge'
import zsgc from '@/components/testInsert/zsgc'
import gptzsgc from '@/components/testInsert/gptzsgc'
import gptzsgc1 from '@/components/testInsert/gptzsgc1'
import jxxtwh from '@/components/jxxt_vue/jxxtwh_vue'

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/stock',
      name: 'MainPage',
      component: mainpage,
      children:[
        {
          path: '/stock/stock',
          name: 'Stock',
          component: stock,
          children:[
            {
              path: '/stock/stockspec',
              name: 'StockSpec',
              component: stockspec
            }
          ]
        }
        ,
        {
          path: '/stock/stockhs300spec',
          name: 'Stockhs300Spec',
          component: stockhs300spec
        },
        {
          path: '/stock/indicator',
          name: 'indicator',
          component: indicator,
          children:[
            {
              path: '/stock/indicatorspec',
              name: 'indicatorspec',
              component: indicatorspec
            }
          ]
        },
      ]
    },
    {
      path: '/empty',
      name: 'Empty',
      component: empty
    },
    {
      path: '/information',
      name: 'information',
      component: information
    },
    {
      path: '/testPAge',
      name: 'testPAge', 
      component: testpage
    },
    {
      path: '/zsgc',
      name: 'zsgc', 
      component: zsgc
    },
    {
      path: '/gptzsgc',
      name: 'gptzsgc', 
      component: gptzsgc
    },
    {
      path: '/gptzsgc1',
      name: 'gptzsgc1', 
      component: gptzsgc1
    }
    ,
    {
      path: '/jxxtwh',
      name: 'jxxtwh', 
      component: jxxtwh
    }

  ]
    
})
