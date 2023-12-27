<template>
  <div class="container">
    <div class="header">
      <h2>交易管理</h2>
      <div class="header-buttons">
        <el-button @click="addNew" type="primary">添加</el-button>
        <el-button @click="submitForm">提交并获取结果</el-button>
        <a href="http://localhost:8000/stockserver/calculate">http://localhost:8000/stockserver/calculate</a>
      </div>

    </div>
    <div class="chart-container">
      <div id="chart" style="width: 600px; height: 400px;"></div>
    </div>
    <el-table :data="list" style="width: 100%">

      <el-table-column label="日期" prop="date"><template slot-scope="scope">{{ formatDate(scope.row.date) }}</template> </el-table-column>



      <el-table-column label="参数" prop="sets"> <template slot-scope="scope">{{scope.row.val}}</template> </el-table-column>

  

      <el-table-column label="操作" width="200">
        <template slot-scope="scope">
          <el-button size="mini" @click="editItem(scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="deleteItem(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog title="编辑" :visible.sync="editDialogVisible">
      <el-form label-position="top" :model="editing">
        <el-form-item label="日期">
          <el-input v-model="editing.date"></el-input>
        </el-form-item>
      </el-form>
      <div class="dialog-footer">
        <el-button @click="cancelEdit">取消</el-button>
        <el-button type="primary" @click="confirmEdit">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
  
<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.dialog-footer {
  text-align: right;
  margin-top: 10px;
}

/* Your existing styles */
.header-buttons {
  display: flex;
  justify-content: flex-end;
}
</style>
<script>
import axios from 'axios'
import * as echarts from 'echarts'; // 导入线图表组件


export default {
  data() {
    return {
      list: [],
      editDialogVisible: false,
      editing: {},
      myChart: null // 添加 myChart 属性
    };
  },
  created() {
    this.list = this.fetchData();
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById('chart')); // 初始化 echarts 实例

    const dates = this.list.map(item => item.date);
    const values = this.list.map(item => item.val);

    // 指定图表的配置项和数据
    var option = {
      title: {
        text: '交易历史'
      },
      tooltip: {},
      xAxis: {
        data: dates
      },
      yAxis: {},
      series: [{
        name: '销量',
        type: 'line',
        data: values
      }]
    };

    // 使用刚指定的配置项和数据显示图表
    this.myChart.setOption(option);
  },
  beforeDestroy() {
    if (this.myChart) {
      this.myChart.dispose(); // 销毁 echarts 实例
    }
  },
  methods: {
    fetchData() {
      return [
        {
          date: "2023-01-01",
          val: "23"
        },
        {
          date: "2023-02-01",
          val: "33"
        },
        {
          date: "2023-03-01",
          val: "34"
        }
      ];
    },
    formatDate(date) {
      //   return date.replace(/-/g, "/");
      // return date;
      if (typeof date === 'string') {
        // 如果 date 已经是字符串类型，直接调用 replace 方法
        return date.replace(/-/g, "/");
      } else if (date instanceof Date) {
        // 如果 date 是 Date 类型，先转换成字符串再调用 replace 方法
        return date.toISOString().replace(/-/g, "/");
      } else {
        // 其他情况，返回空字符串或者抛出错误，视情况而定
        return '';
      }
    },

    updateChart() {
      const dates = this.list.map(item => item.date);
      const values = this.list.map(item => item.val);

      // 指定图表的配置项和数据
      var option = {
        title: {
          text: '交易历史'
        },
        tooltip: {},
        xAxis: {
          data: dates
        },
        yAxis: {},
        series: [{
          name: '销量',
          type: 'line',
          data: values
        }]
      };

      // 使用刚指定的配置项和数据显示图表
      this.myChart.setOption(option);
    },
    addNew() {
      const date = new Date().toISOString().substring(0, 10);
      const val = (Math.floor(Math.random() * 50) + 20).toString();

      this.list.push({ date, val });
      //   console.log(this.list);
      this.updateChart();
      //   console.log(this.list);
      //   this.$nextTick(() => {});
    },
    deleteItem(row) {
      this.list = this.list.filter(item => item !== row);
      this.updateChart();
    },
    editItem(row) {
      this.editing = row;
      this.editDialogVisible = true;
      this.updateChart();
    },
    cancelEdit() {
      this.editing = {};
      this.editDialogVisible = false;
    },
    confirmEdit() {
      this.editDialogVisible = false;
      const index = this.list.findIndex(item => item.date === this.editing.date);
      this.$set(this.list, index, this.editing);
      this.editing = {};
    },
    //Post貌似走不通，先不走了，后续再说
    // submitForm() {
    //   // alert(this.stockCode)
    //   // const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    //   let params = {
    //     stockCode: 'ABC', // 替换为实际的股票代码
    //     startDate: '2023-01-01', // 替换为实际的起始日期
    //     endDate: '2023-12-31' // 替换为实际的结束日期
    //   }
    //   alert(params.endDate)

    //   // /stockserver/calculate/
    //   axios.post("http://localhost:8000/stockserver/calculate/", params, {withCredentials: true})
    //     .then(response => {
    //       // alert("turn")

    //       // 获取接口返回的指标数据
    //       let indicators = response.data.data.indicators


    //       // 传给结果组件
    //       this.$emit('show-result', indicators)
    //       alert("false")

    //     })
    // }
      //通过get方式进行传递数据
    submitForm() {
      // alert(this.stockCode)
      // const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      let params = {
        stockCode: 'ABC', // 替换为实际的股票代码
        startDate: '2023-01-01', // 替换为实际的起始日期
        endDate: '2023-12-31' // 替换为实际的结束日期
      }
      alert(params.endDate)

      // /stockserver/calculate/
      axios.get("http://localhost:8000/stockserver/calculate/", {params})
        .then(response => {
          // alert("turn")
          // 获取接口返回的指标数据
          let indicators = response.data.keys;
          alert(indicators)
        })
    }

  }
};
</script>
