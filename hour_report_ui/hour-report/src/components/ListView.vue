<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface FormData {
  subject: string
  selectedOption: string
  time: string
  comment: string
}

const submissions = ref<FormData[]>([])
const options = [
  { value: 'option1', label: 'گزینه ۱' },
  { value: 'option2', label: 'گزینه ۲' },
  { value: 'option3', label: 'گزینه ۳' }
]

onMounted(() => {
  const savedData = localStorage.getItem('submissions')
  if (savedData) {
    submissions.value = JSON.parse(savedData)
  }
})
</script>

<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-body">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <router-link to="/" class="btn btn-primary">بازگشت به فرم</router-link>
              <h2 class="card-title m-0">لیست اطلاعات</h2>
            </div>
            
            <div class="list-group" v-if="submissions.length > 0">
              <div v-for="(item, index) in submissions" :key="index" class="list-group-item">
                <h5 class="mb-2">{{ item.subject }}</h5>
                <p class="mb-1">
                  <strong>گزینه انتخابی:</strong> 
                  {{ options.find(opt => opt.value === item.selectedOption)?.label }}
                </p>
                <p class="mb-1"><strong>زمان:</strong> {{ item.time }}</p>
                <p class="mb-0"><strong>توضیحات:</strong> {{ item.comment }}</p>
              </div>
            </div>
            <div v-else class="text-center text-muted py-4">
              هنوز اطلاعاتی ثبت نشده است
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.list-group-item {
  text-align: right;
}
</style>