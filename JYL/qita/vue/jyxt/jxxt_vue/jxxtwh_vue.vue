<template>
    <div class="container">
        <div class="header">
            <h2>交易管理</h2>
            <div class="header-buttons">
                <el-button @click="showInputDialog" type="primary">添加记录</el-button>
                <el-dialog title="添加交易记录" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
                    <el-form :model="formData" label-width="100px">
                        <el-form-item label="股票代码" prop="stockcode">
                            <el-input v-model="formData.stockcode"></el-input>
                        </el-form-item>
                        <el-form-item label="股票名称" prop="stockName">
                            <el-input v-model="formData.stockName"></el-input>
                        </el-form-item>
                        <el-form-item label="交易时间" prop="tradeTime">
                            <el-date-picker v-model="formData.tradeTime" type="date"></el-date-picker>
                        </el-form-item>
                        <el-form-item label="交易方向" prop="direction">
                            <el-select v-model="formData.direction" placeholder="请选择">
                                <el-option label="买入" value="buy"></el-option>
                                <el-option label="卖出" value="sell"></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="交易数量" prop="volume">
                            <el-input v-model="formData.volume"></el-input>
                        </el-form-item>
                        <el-form-item label="交易价格" prop="price">
                            <el-input v-model="formData.price"></el-input>
                        </el-form-item>
                        <el-form-item label="交易额" prop="turnover">
                            <el-input v-model="formData.turnover"></el-input>
                        </el-form-item>
                        <el-form-item label="佣金" prop="commissionFee">
                            <el-input v-model="formData.commissionFee"></el-input>
                        </el-form-item>
                        <el-form-item label="印花税" prop="stampDuty">
                            <el-input v-model="formData.stampDuty"></el-input>
                        </el-form-item>
                        <el-form-item label="过户费" prop="transferFee">
                            <el-input v-model="formData.transferFee"></el-input>
                        </el-form-item>
                        <el-form-item label="交易金额" prop="amount">
                            <el-input v-model="formData.amount"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitFormnew">提交</el-button>
                            <el-button @click="closeDialog">取消</el-button>
                        </el-form-item>
                    </el-form>
                </el-dialog>
                <el-select v-model="selectedValue" placeholder="请选择数值" @change="handleSelectChange">
                    <el-option v-for="item in selectOptions" :key="item" :label="item" :value="item"></el-option>
                </el-select>
                <el-button @click="submitForm" type="primary">提交并获取结果</el-button>
            </div>
        </div>
        <div class="chart-container">
            <div id="chart" style="width: 100%; height: 400px;"></div>
        </div>
        <el-table :data="list" style="width: 100%">
            <el-table-column prop="id" label="交易次数">
                <template slot-scope="scope">
                    {{ scope.row.id }}
                </template>
            </el-table-column>
            <el-table-column prop="stockName" label="股票名称">
                <template slot-scope="scope">
                    {{ scope.row.stockName }}
                </template>
            </el-table-column>
            <el-table-column prop="stockcode" label="股票代码">
                <template slot-scope="scope">
                    {{ scope.row.stockcode }}
                </template>
            </el-table-column>
            <el-table-column prop="tradeTime" label="成交时间">
                <template slot-scope="scope">
                    {{ scope.row.tradeTime }}
                </template>
            </el-table-column>
            <el-table-column prop="direction" label="买卖方向">
                <template slot-scope="scope">
                    {{ scope.row.direction }}
                </template>
            </el-table-column>
            <el-table-column prop="volume" label="成交数量">
                <template slot-scope="scope">
                    {{ scope.row.volume }}
                </template>
            </el-table-column>
            <el-table-column prop="price" label="成交价格">
                <template slot-scope="scope">
                    {{ scope.row.price }}
                </template>
            </el-table-column>
            <el-table-column prop="turnover" label="成交金额">
                <template slot-scope="scope">
                    {{ scope.row.turnover }}
                </template>
            </el-table-column>
            <el-table-column prop="commissionFee" label="手续费">
                <template slot-scope="scope">
                    {{ scope.row.commissionFee }}
                </template>
            </el-table-column>
            <el-table-column prop="stampDuty" label="印花税">
                <template slot-scope="scope">
                    {{ scope.row.stampDuty }}
                </template>
            </el-table-column>
            <el-table-column prop="transferFee" label="过户费">
                <template slot-scope="scope">
                    {{ scope.row.transferFee }}
                </template>
            </el-table-column>
            <el-table-column prop="amount" label="发生金额合计">
                <template slot-scope="scope">
                    {{ scope.row.amount }}
                </template>
            </el-table-column>

            <el-table-column label="操作" width="200">
                <template slot-scope="scope">
                    <el-button size="mini" @click="editItem(scope.row)">编辑</el-button>
                    <el-button size="mini" type="danger" @click="deleteItem(scope.row.id)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>


        <el-dialog title="编辑交易" :visible.sync="editDialogVisible" width="500px">

            <el-form :model="editing">

                <el-form-item label="交易次数">
                    <el-input v-model="editing.id"></el-input>
                </el-form-item>

                <el-form-item label="股票代码">
                    <el-input v-model="editing.stockcode"></el-input>
                </el-form-item>

                <el-form-item label="股票名称">
                    <el-input v-model="editing.stockName"></el-input>
                </el-form-item>

                <el-form-item label="交易日期">
                    <el-date-picker v-model="editing.tradeTime" type="date"></el-date-picker>
                </el-form-item>

                <el-form-item label="交易方向">
                    <el-select v-model="editing.direction">
                        <el-option label="买入" value="buy"></el-option>
                        <el-option label="卖出" value="sell"></el-option>
                    </el-select>
                </el-form-item>

                <el-form-item label="成交数量">
                    <el-input-number v-model="editing.volume"></el-input-number>
                </el-form-item>

                <el-form-item label="成交价格">
                    <el-input-number v-model="editing.price"></el-input-number>
                </el-form-item>

                <el-form-item label="成交金额">
                    <el-input-number v-model="editing.turnover"></el-input-number>
                </el-form-item>

                <el-form-item label="手续费">
                    <el-input-number v-model="editing.commissionFee"></el-input-number>
                </el-form-item>

                <el-form-item label="印花税">
                    <el-input-number v-model="editing.stampDuty"></el-input-number>
                </el-form-item>

                <el-form-item label="过户费">
                    <el-input-number v-model="editing.transferFee"></el-input-number>
                </el-form-item>

                <el-form-item label="发生金额合计">
                    <el-input-number v-model="editing.amount"></el-input-number>
                </el-form-item>

            </el-form>

            <div slot="footer">
                <el-button @click="cancelEdit">取消</el-button>
                <el-button type="primary" @click="updateEditing(editing)">保存</el-button>
            </div>

        </el-dialog>



    </div>
</template>
    
<style>
.container {
    max-width: 100%;
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
import common from './common.vue'


export default {
    data() {
        return {
            list: [],// 列表
            editDialogVisible: false,// 添加记录框是否展示            
            dialogVisible: false,// 编辑框是否展示
            editing: {},
            myChart: null,// 添加 myChart 属性
            selectedValue: '', // 新增的属性，用于存储选定的数值
            selectOptions: [], // 新增的属性，下拉单选框的选项数组
            editing: {},
            formData: {
                stockcode: '23',
                stockName: '32',
                tradeTime: '2023-12-05',
                direction: 'buy',
                volume: '1000',
                price: '21',
                turnover: '0',
                commissionFee: '0',
                stampDuty: '0',
                transferFee: '0',
                amount: '322'
            }
        };
    },
    created() {
        this.list = this.fetchData();

    },
    mounted() {
        this.myChart = echarts.init(document.getElementById('chart')); // 初始化 echarts 实例     
        // 使用刚指定的配置项和数据显示图表
        this.myChart.setOption(option);
    },
    beforeDestroy() {
        if (this.myChart) {
            this.myChart.dispose(); // 销毁 echarts 实例
        }
    },
    methods: {
        // showInputDialog() 方法用于显示对话框，将 dialogVisible 属性设置为 true，从而显示添加交易记录的对话框。
        // handleClose(done) 方法用于处理对话框关闭的逻辑。它使用 this.$confirm 方法显示一个确认对话框，当用户确认关闭时，调用 done() 方法关闭对话框。
        // closeDialog() 方法用于关闭对话框，将 dialogVisible 属性设置为 false，从而隐藏对话框。
        // submitForm() 方法用于提交表单数据到后台 Django。它使用 Axios 或其他方式发送 POST 请求到后台接口 / api / addTransaction，并根据后台返回的结果进行相应的处理。如果提交成功，显示添加成功的消息，并关闭对话框；如果提交失败，显示添加失败的消息。
        showInputDialog() {
            this.dialogVisible = true;
        },
        // handleClose(done) {
        //     this.$confirm('确认关闭？')
        //         .then(_ => {
        //             done();
        //         })
        //         .catch(_ => { });
        // },
        closeDialog() {
            this.dialogVisible = false;
        },
        submitFormnew() {
            // 将 this.formData 中的数据提交到后台 Django
            // 使用 axios 或其他方式发送 POST 请求
            // 示例：假设后台接口为 /api/addTransaction
            let params = this.formData;
            // alert(params.tradeTime);
            axios.get(common.django_url + "/stockserver/jxxtnewinsert/", { params })
                .then(response => {
                    // 处理成功响应
                    // alert("成功")
                    // 刷新交易记录列表等操作
                })
                .catch(error => {
                    // 处理错误
                    this.$message.error('添加失败');
                });
        },
        fetchData() {
            // alert(1)
            axios.get(common.django_url + "/stockserver/firstjxxt/")
                .then(response => {
                    // alert(2)
                    this.list = JSON.parse(response.data.data1);

                    this.selectOptions = response.data.data2;

                    this.updateChart();
                    // alert(this.list.map(item => item.stockName)[0])
                    this.selectedValue = this.list.map(item => item.stockName)[0];
                })
            return data;
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
            // let buyData = [];
            // let sellData = [];

            let syx=0;
            let syxz=[];
            // let gd=0;
            //区分买卖后，进行分组
            // this.list.forEach(item => {
            //     if (item.direction === 'buy') {
            //         buyData.push(item.amount);
            //     } else {
            //         sellData.push(item.amount);
            //     }
            // })
            this.list.forEach(item => {
                if(item.direction==='buy'){                    
                    syx=syx+item.amount;
                    syxz.push(syx);
                }else{
                    syx=syx-item.amount;
                    syxz.push(syx);
                }
            });
            syxz= syxz.map(x=>x.toFixed(2));        
            const dates = this.list.map(item => item.tradeTime);
            // const values = syxz.map(item => item.amount);
            let maxyprice = (Math.max(...syxz) + 1).toFixed(3);
            let minyprice = (Math.min(...syxz) - 1).toFixed(3);
            // alert("maxyprice"+maxyprice);
            // alert(minyprice);
            // const averages = [];
            // let sum = 0;

            // for (let i = 0; i < values.length; i++) {
            //     sum += values[i];
            //     const average = sum / (i + 1);
            //     averages.push(average.toFixed(3));
            // }
            // const line3 = averages.map(value => value + 1); // 计算第三条折线的数据

            // 指定图表的配置项和数据
            var option = {
                title: {
                    text: '交易历史'
                },
                tooltip: {},
                xAxis: {
                    data: dates
                },
                yAxis: {
                    type: 'value',
                    min: minyprice,
                    max: maxyprice
                },
                series: [
                    // {
                    //     name: '买入价',
                    //     type: 'line',
                    //     data: buyData,
                    //     label: {
                    //         show: true,  // 显示标签
                    //         position: 'top'  // 标签位置，可以根据需要调整
                    //     }
                    // },
                    // {
                    //     name: '卖出价',
                    //     type: 'line',
                    //     data: sellData,
                    //     label: {
                    //         show: true,  // 显示标签
                    //         position: 'top'  // 标签位置，可以根据需要调整
                    //     }
                    // },
                    {
                        name: '剩余线',
                        type: 'line',
                        data: syxz,
                        label: {
                            show: true,  // 显示标签
                            position: 'top'  // 标签位置，可以根据需要调整
                        }
                    },
                ]
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
        deleteItem(uuid) {
            // this.list = this.list.filter(item => item !== row);
            let params = { key: uuid }
            axios.get(common.django_url + "/stockserver/jxxtwhdelete/", { params })
                .then(response => {
                    alert("删除成功" + uuid)
                    // this.list = JSON.parse(response.data.data1);
                    // this.updateChart();
                    this.submitForm()
                })



        },
        // editItem(row) {
        //     this.editing = row;
        //     this.editDialogVisible = true;
        //     this.updateChart();
        // },
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
        //   初始化页面
        firstinit() {

        },
        submitForm() {
            let params = {
                stockname: this.selectedValue, // 将选定的数值传递到后端                
            }
            axios.get(common.django_url + "/stockserver/SubmitButton/", { params })
                .then(response => {
                    this.list = JSON.parse(response.data.data1);
                    // let price = list.map(item => item.price)



                    this.selectOptions = response.data.data2;
                    this.updateChart();
                    this.selectedValue = this.list.map(item => item.stockName)[0];
                })
        },
        // 编辑修改功能从此开始
        // 点击编辑功能
        editItem(row) {
            // 先复制行数据到 editing
            this.editing = Object.assign({}, row);
            this.editDialogVisible = true;
        },
        // // 保存更新数据
        updateEditing(row) {
            let params = {
                id: row.id,
                stockcode: row.stockcode,
                stockName: row.stockName,
                tradeTime: row.tradeTime,
                direction: row.direction,
                volume: row.volume,
                price: row.price,
                turnover: row.turnover,
                commissionFee: row.commissionFee,
                stampDuty: row.stampDuty,
                transferFee: row.transferFee,
                amount: row.amount
            }
            // 调用接口更新数据
            axios.get(common.django_url + "/stockserver/updateEditing/", { params }).then(res => {
                if (res.status === 200) {
                    // 刷新列表
                    this.fetchData();
                    // 关闭编辑框
                    this.editDialogVisible = false;
                }
            })
        },
        confirmEdit() {
            this.updateEditing(this.editing);
        },

        editItem(row) {
            // 先复制行数据到 editing
            this.editing = Object.assign({}, row);
            this.editDialogVisible = true;
        }
    }
};
</script>
  