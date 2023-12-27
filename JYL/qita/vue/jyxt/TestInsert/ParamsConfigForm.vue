<script>
import axios from 'axios'

methods: {

  submitForm() {
    
    let params = {
       stockCode: this.stockCode 
    }
    
    axios.post('/api/calculate', params)
      .then(response => {

        // 获取接口返回的指标数据
        let indicators = response.data.data.indicators

        // 传给结果组件
        this.$emit('show-result', indicators)  

      })
  }

}
</script>