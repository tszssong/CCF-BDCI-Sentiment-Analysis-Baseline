export CUDA_VISIBLE_DEVICES=0,1,2,3
mkdir ./model_bert_wwm_ext_news
python run_bert.py \
--model_type bert \
--model_name_or_path ./chinese_wwm_ex_bert \
--do_train \
--do_eval \
--data_dir ./news \
--output_dir ./model_bert_wwm_ext_news \
--max_seq_length 256 \
--split_num 3 \
--lstm_hidden_size 512 \
--lstm_layers 1 \
--lstm_dropout 0.1 \
--eval_steps 1000 \
--per_gpu_train_batch_size 1 \
--gradient_accumulation_steps 1 \
--warmup_steps 0 \
--per_gpu_eval_batch_size 32 \
--learning_rate 5e-6 \
--adam_epsilon 1e-6 \
--weight_decay 0 \
--num-classes 12 \
--train_steps 5000 2>&1 |tee ./model_bert_wwm_ext_news/log
