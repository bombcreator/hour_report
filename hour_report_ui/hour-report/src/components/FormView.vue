<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

interface FormData {
  subject: string
  selectedOption: string
  time: string
  comment: string
}

const router = useRouter()
const subject = ref('')
const selectedOption = ref('option1')
const timeInput = ref('')
const comment = ref('')

// Get existing submissions from localStorage or initialize empty array
const existingData = localStorage.getItem('submissions')
const submissions = ref<FormData[]>(existingData ? JSON.parse(existingData) : [])

const options = [
  { value: 'option1', label: 'گزینه ۱' },
  { value: 'option2', label: 'گزینه ۲' },
  { value: 'option3', label: 'گزینه ۳' }
]

const handleSubmit = () => {
  const newSubmission: FormData = {
    subject: subject.value,
    selectedOption: selectedOption.value,
    time: timeInput.value,
    comment: comment.value
  }
  submissions.value.push(newSubmission)
  
  // Save to localStorage
  localStorage.setItem('submissions', JSON.stringify(submissions.value))
  
  // Reset form
  subject.value = ''
  selectedOption.value = 'option1'
  timeInput.value = ''
  comment.value = ''

  // Navigate to list view
  router.push('/list')
}
</script>

<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-body">
            <h2 class="card-title mb-4 text-center">فرم ساده</h2>
            <form @submit.prevent="handleSubmit" dir="rtl">
              <div class="mb-3">
                <label for="subject" class="form-label">موضوع:</label>
                <input 
                  type="text" 
                  id="subject" 
                  v-model="subject"
                  class="form-control"
                  placeholder="موضوع را وارد کنید..."
                  required
                >
              </div>

              <div class="mb-3">
                <label for="dropdown" class="form-label">انتخاب کنید:</label>
                <select 
                  id="dropdown" 
                  v-model="selectedOption"
                  class="form-select"
                  required
                >
                  <option v-for="option in options" :key="option.value" :value="option.value">
                    {{ option.label }}
                  </option>
                </select>
              </div>

              <div class="mb-3">
                <label for="time" class="form-label">زمان (HH:mm):</label>
                <input 
                  type="time" 
                  id="time" 
                  v-model="timeInput"
                  class="form-control"
                  required
                >
              </div>

              <div class="mb-3">
                <label for="comment" class="form-label">توضیحات:</label>
                <textarea 
                  id="comment" 
                  v-model="comment"
                  rows="4"
                  class="form-control"
                  placeholder="توضیحات خود را اینجا وارد کنید..."
                  required
                ></textarea>
              </div>

              <div class="d-flex gap-2">
                <button type="submit" class="btn btn-primary flex-grow-1">ارسال</button>
                <router-link to="/list" class="btn btn-secondary">مشاهده لیست</router-link>
              </div>
            </form>
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
</style>