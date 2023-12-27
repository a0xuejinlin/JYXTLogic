<template>
    <div>
   
     <el-button @click="addNew">添加</el-button>
   
     <el-table :data="list">
      <el-table-column label="日期" prop="date">
        <template slot-scope="scope">
          {{ formatDate(scope.row.date) }}
        </template>
      </el-table-column>
   
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="editItem(scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="deleteItem(scope.row)">删除</el-button>  
        </template>
      </el-table-column>
     </el-table>
   
   
     <el-dialog title="编辑" :visible.sync="editDialogVisible">
       <el-form label-position="left" label-width="80px">
         <el-form-item label="日期">
           <el-input v-model="editing.date"></el-input>
         </el-form-item>
       </el-form>
       <div slot="footer">
         <el-button @click="cancelEdit">取消</el-button>
         <el-button type="primary" @click="confirmEdit">确定</el-button>
       </div>
     </el-dialog>
   
    </div>
   </template>
   
   <script>  
   export default {
   
     data() {
       return {
         list: [],
         editDialogVisible: false,
         editing: {} 
       }
     },
   
     created() {
       this.list = this.fetchData()
     },
   
     methods: {
       
       fetchData() { 
         return [{
           date: '2023-01-01'  
         },{
           date: '2023-02-01' 
         }]
       },
   
       formatDate(date) {
         return date.replace(/-/g, '/')
       },
   
       addNew() {
         const date = new Date().toISOString()   
         this.list.push({
           date  
         })
       },
   
       deleteItem(row) {
         this.list = this.list.filter(item => item !== row)  
       },
   
       editItem(row) {
         this.editing = row
         this.editDialogVisible = true
       },
       
       cancelEdit() {
         this.editing = {}
         this.editDialogVisible = false  
       },
       
       confirmEdit() {
         this.editDialogVisible = false
         
         const index = this.list.findIndex(item => item === this.editing)
         this.list.splice(index, 1, this.editing)
         
         this.editing = {} 
       }
       
     }
   
   }
   </script>