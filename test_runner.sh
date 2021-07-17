
set -e
set -x

# ENV
pwd
#which ruby

# RVM
#source ./rvm-setup.sh

# Type
#FEATURES=$(find features/* -type d -maxdepth 0 -path features/data_feed_billing -prune -o -path features/batch_output -prune -o  -path features/support -prune -o -path features/step_definitions -prune -o  -path features/ui -prune -o -path features/eba_jobs -prune -o -print)
#
#TYPE=$1
#if [[ "$TYPE" == 'UI_EMPLOYEE' ]]; then
#  FEATURES="${FEATURES} features/ui/employee"
#elif [[ "$TYPE" == 'UI_SALARY_BENEFIT' ]]; then
#  FEATURES="${FEATURES} features/ui/salary features/ui/benefit"
#elif [[ "$TYPE" == 'UI_UPLOAD_EMPLOYEE' ]]; then
#  FEATURES="${FEATURES} features/ui/upload_employee_data"
#elif [[ "$TYPE" == 'UI_REST_AND_JOBS' ]]; then
#  UI_REST=$(find features/eba_jobs/* features/batch_output/* features/ui/* -type d -maxdepth 0 -path features/ui/employee -prune -o -path features/ui/benefit -prune -o -path features/ui/salary -prune -o -path features/ui/upload_employee_data -prune -o -print)
#  FEATURES="${FEATURES} ${UI_REST}"
#elif [[ "$TYPE" == 'UI' ]]; then
#  FEATURES="${FEATURES} features/ui"
#elif [[ "$TYPE" == 'DFB_BENEFIT' ]]; then
#  FEATURES="${FEATURES} features/data_feed_billing/benefit"
#elif [[ "$TYPE" == 'DFB_EMPLOYEE_CBDC' ]]; then
#  FEATURES="${FEATURES} features/data_feed_billing/employee/change_billing_category features/data_feed_billing/employee/change_billing_division"
#elif [[ "$TYPE" == 'DFB_EMPLOYEE_REST' ]]; then
#  DFB_EMPLOYEE_REST=$(find features/data_feed_billing/employee/* -type d -maxdepth 0 -path features/data_feed_billing/employee/change_billing_category -prune -o -path features/data_feed_billing/employee/change_billing_division -prune -o -print)
#  FEATURES="${FEATURES} ${DFB_EMPLOYEE_REST}"
#elif [[ "$TYPE" == 'DFB_EMPLOYEE' ]]; then
#  FEATURES="${FEATURES} features/data_feed_billing/employee"
#elif [[ "$TYPE" == 'DFB_REST' ]]; then
#  DFB_REST=$(find features/data_feed_billing/* -type d -maxdepth 0 -path features/data_feed_billing/benefit -prune -o -path features/data_feed_billing/employee -prune -o -print)
#  FEATURES="${FEATURES} ${DFB_REST}"
#elif [[ "$TYPE" == 'DFB' ]]; then
#  FEATURES="${FEATURES} features/data_feed_billing"
#else
#  FEATURES='features'
#fi

# Run BBOX
#if [[ "$CI" == 'true' ]]; then
#  BLACKBOX_ENV=ci
#else
#  BLACKBOX_ENV=${BLACKBOX_ENV:=development}
#fi

echo "------------------------------------------------------------------------------"
#echo BlackBox Runtime Environment: ${ENV}
#echo Pass CI=true or BLACKBOX_ENV=ci/development/local if you want to use another environment.
echo "------------------------------------------------------------------------------"


#unamestr=$(uname)
#if [[ "$unamestr" == 'Darwin' ]]; then
#  BLACKBOX_ENV=${BLACKBOX_ENV} rvm ${RVM_RUBY}@${RVM_GEMSET} do bundle exec  cucumber $FEATURES -p ci --retry 1
#else
#  BLACKBOX_ENV=${BLACKBOX_ENV} rvm ${RVM_RUBY}@${RVM_GEMSET} do bundle exec cucumber $FEATURES -p ci || BLACKBOX_ENV=${BLACKBOX_ENV} rvm ${RVM_RUBY}@${RVM_GEMSET} do bundle exec cucumber -p ci_rerun --retry 1
#fi
#rerun last failure
pytest ||  pytest --lf
